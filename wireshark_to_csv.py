import pyshark
import pandas as pd
import os

# Path to the PCAP file
pcap_file = r""

# Path to the output file
output_csv = 'distinct_combinations_pcap.csv'

# Check if PCAP file exists
if not os.path.isfile(pcap_file):
    print(f"Error: File '{pcap_file}' not found.")
    exit(1)

# Define the fields to extract from the packets
fields = ['ip.src', 'ip.dst', 'frame.protocols', 'frame.len', 'frame.info']

# List to store packet information
packets_data = []

print(f"Loading PCAP file '{pcap_file}'...")

try:
    # Open and parse the PCAP file
    # decode_as parameter ensures HTTP traffic on port 80 is properly decoded
    cap = pyshark.FileCapture(pcap_file, keep_packets=False, decode_as={'tcp.port==80':'http'})
except Exception as e:
    print(f"Error opening PCAP file: {e}")
    exit(1)

print("Extracting packets...")

for packet in cap:
    packet_info = {}
    try:
        # Extract required fields from each packet
        # Basic network information like source, destination IP, protocol, etc.
        packet_info['Source'] = packet.ip.src
        packet_info['Destination'] = packet.ip.dst
        packet_info['Protocol'] = packet.transport_layer  # e.g., TCP, UDP
        packet_info['Length'] = packet.length
        packet_info['Info'] = packet.info if hasattr(packet, 'info') else ''
        packets_data.append(packet_info)
    except AttributeError:
        # Skip packets that don't have all required fields
        continue

cap.close()
print(f"Extraction completed. Processed {len(packets_data)} packets.")

# Create DataFrame from collected packet data
df = pd.DataFrame(packets_data)

# Remove duplicate entries to get unique combinations
df_unique = df.drop_duplicates()

# Count unique combinations
unique_count = df_unique.shape[0]
print(f"Number of unique combinations: {unique_count}")

# Save unique combinations to CSV file
try:
    df_unique.to_csv(output_csv, index=False)
    print(f"Unique combinations successfully saved to '{output_csv}'.")
except Exception as e:
    print(f"Error saving file '{output_csv}': {e}")
    exit(1)
# 🦈 WireDistinct

> Convert Wireshark captures into clean, deduplicated CSV reports with zero effort.

WireDistinct is a streamlined Python tool that transforms verbose Wireshark packet captures into concise CSV reports, showing only distinct network communication patterns. Perfect for network analysts who need a quick overview of unique traffic patterns without the noise of repeated packets.

## ✨ What It Does

Turns this:
```
Thousands of packet captures with redundant information...
```

Into this:
```
Source IP | Destination IP | Protocol | Length | Info
---------|---------------|-----------|---------|------
10.0.0.1 | 192.168.1.1  | TCP       | 64      | SYN
...
```

## 🎯 Key Features

- **Deduplication**: Automatically removes redundant packet combinations
- **Smart Filtering**: Extracts essential network metadata
- **Fast Processing**: Efficiently handles large PCAP files
- **Clean Output**: Generates analysis-ready CSV reports

## 🚀 Quick Start

1. Install dependencies:
```bash
pip install pyshark pandas
```

2. Run the script:
```python
python wiredistinct.py
```

3. Find your cleaned data in `distinct_combinations_pcap.csv`

## 📊 Output Format

The generated CSV includes these key fields:
- Source IP Address
- Destination IP Address
- Protocol Type
- Packet Length
- Additional Packet Information

## 💻 Requirements

- Python 3.x
- pyshark
- pandas
- Wireshark installed on your system

## 🛠️ Configuration

Update the PCAP file path in the script:
```python
pcap_file = "path/to/your/wireshark/capture.pcapng"
```


## 📝 License

MIT License - feel free to use in your projects!

---
Made with ☕ and Python
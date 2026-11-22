import asyncio
import pyshark
import pandas as pd


def capture_packets(interface='WiFi', packet_count=5000):
    # Create event loop manually (required for Python 3.14)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    capture = pyshark.LiveCapture(interface=interface, eventloop=loop)
    packets = []

    for packet in capture.sniff_continuously(packet_count=packet_count):
        try:
            packets.append({
                'timestamp': packet.sniff_time,
                'protocol': packet.highest_layer,
                'length': int(packet.length)
            })
        except Exception as e:
            print(f"Error processing packet: {e}")
            continue

    capture.close()
    loop.close()

    return packets


if __name__ == "__main__":
    print("Starting packet capture...\n")

    data = capture_packets(packet_count=5000)

    df = pd.DataFrame(data)
    df.to_csv("captured_data.csv", index=False)

    print("Capture complete.")
    print("Saved to captured_data.csv")
    print(f"Total packets captured: {len(df)}")

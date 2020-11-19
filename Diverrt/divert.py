import pydivert

with pydivert.WinDivert("udp.SrcPort == 50225",layer=0) as w:
    for packet in w:
        if packet.is_outbound:
            packet.dst_addr = "192.168.43.48"
            packet.src_addr = "192.168.43.22"
            print("packeeet")
            print(packet)
            w.send(packet)

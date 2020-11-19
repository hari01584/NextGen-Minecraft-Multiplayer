import pydivert


rw = b"4500003d3c7c4000401126a3c0a82b10c0a82b30d81c27170029578a01000000000005df2200ffff00fefefefefdfdfdfd1234567880b99ff534a4b5ae"
with pydivert.WinDivert("udp.DstPort == 10007",layer=0) as w:
    packet = pydivert.Packet(rw,(8, 0),pydivert.Direction.INBOUND)
    w.send(packet)
    for packet in w:
        print(packet.raw.hex())
        w.send(packet)

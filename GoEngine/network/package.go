package network

import (
	my_go "GoEngine/proto"
	"encoding/binary"

	"fmt"

	"google.golang.org/protobuf/proto"
)

// 封装 Protobuf 数据包
func EncodePacket(msgID uint16, pb proto.Message) ([]byte, error) {
	body, err := proto.Marshal(pb)
	if err != nil {
		return nil, err
	}
	packet := make([]byte, 4+len(body))
	binary.BigEndian.PutUint16(packet[0:2], msgID)
	binary.BigEndian.PutUint16(packet[2:4], uint16(len(body)))
	copy(packet[4:], body)
	return packet, nil
}

// 解包 Protobuf 数据包
func DecodePacket(data []byte) (msgID uint16, payload proto.Message, err error) {
	if len(data) < 4 {
		return 0, nil, fmt.Errorf("invalid packet")
	}
	msgID = binary.BigEndian.Uint16(data[0:2])
	length := binary.BigEndian.Uint16(data[2:4])
	if int(length) != len(data[4:]) {
		return 0, nil, fmt.Errorf("length mismatch")
	}
	payload = &my_go.UserMove{} // 默认解包为 UserMove，可以根据 msgID 动态选择
	if err := proto.Unmarshal(data[4:], payload); err != nil {
		return 0, nil, fmt.Errorf("failed to unmarshal: %v", err)
	}
	return
}
tap_tcp = Listener.new(nil, "tcp")

f_flags = Field.new("tcp.flags")

-- Packet handler
function tap_tcp.packet(pinfo, buf)
	-- When called, the `f_flags` field extracts `tcp.flags` from
	-- the current packet and returns a `FieldInfo` object.
	f = f_flags()
	if f then
		print(string.format("tcp.flags = %#x", f.value))
	end
end

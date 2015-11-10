-- tshark -q -X lua_script:hsrp-hash-tap.lua -r test.pcap
-- https://wiki.wireshark.org/Lua/Taps

tap_hsrp = Listener.new(nil, "hsrp")

f_hash = Field.new("hsrp.hash")

function tap_hsrp.packet(pinfo, buf)
	local f = f_hash()
	if f then
		print(string.format("%d:%s", pinfo.number, f.value))
	end
end

function tap_hsrp.draw()
end

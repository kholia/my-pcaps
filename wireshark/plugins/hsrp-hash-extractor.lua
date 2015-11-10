-- extract HSRP hashes, based on https://wiki.wireshark.org/Lua/Dissectors

hash_f = Field.new("hsrp.hash")

-- declare our (pseudo) protocol
my_proto = Proto("HSRP-hash-extractor", "HSRP hash extractor")

-- create the fields for our protocol
hash_F = ProtoField.string("HSRP-hash-extractor.hash", "HSRP hash")

-- add the field to the protocol
my_proto.fields = { hash_F }

-- create a function to "postdissect" each frame
function my_proto.dissector(buffer,pinfo,tree)
	-- obtain the current value of the protocol fields
	local hash = hash_f()
	if hash then
		print(string.format("%d:%s", pinfo.number, hash))
	end
end

-- register our protocol as a postdissector
register_postdissector(my_proto)

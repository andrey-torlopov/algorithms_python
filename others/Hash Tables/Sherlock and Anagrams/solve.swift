//Not optimal!

extension Character {
	var isAscii: Bool {
		return unicodeScalars.allSatisfy { $0.isASCII }
	}
	var ascii: UInt32? {
		return isAscii ? unicodeScalars.first?.value : nil
	}
}

func sherlockAndAnagrams(s: String) -> Int {
	let startChar = Unicode.Scalar("a").value
	let endChar = Unicode.Scalar("z").value
	let alphabet = (startChar...endChar).map { return String(Unicode.Scalar($0)!) }


	var signatures: [String: Int] = [:]
	var signature = Array(repeating: 0, count: alphabet.count)

	s.forEach { signature[Int($0.asciiValue! - Character(alphabet[0]).asciiValue!)] += 1  }

	for start in 0..<s.count {
		for finish in start..<s.count {
			var signature = Array(repeating: 0, count: alphabet.count)
			for index in start..<finish+1 {
				let letter = Array(s)[index]
				signature[Int(letter.ascii! - Character(alphabet[0]).ascii!)] += 1
			}
			let signatureKey = signature.map { return String($0) }.joined()
			let val = signatures[signatureKey] ?? 0
			signatures[signatureKey] = val + 1
		}
	}

	var result = 0
	for count in signatures.values {
		result += count*(count - 1) / 2
	}
	return result
}

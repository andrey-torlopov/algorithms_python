
let s1 = "hello"
let s2 = "world"

func twoStrings(s1: String, s2: String) {
	var s1Ary = Array(s1)
	var s2Ary = Array(s2)
	
	var h: [String: Int] = [:]
	var result = "No"
	
	for i in 0..<max(s1Ary.count, s2Ary.count) {
		if i < s1Ary.count {
			let l1 = String(s1Ary[i])
			if h[l1] == nil {
				h[l1] = 1
			}
			else if let value = h[l1], value < 0 {
				result = "Yes"
				break
			}
		}
		
		if i < s2Ary.count {
			let l2 = String(s2Ary[i])
			if h[l2] == nil {
				h[l2] = -1
			}
			else if let value = h[l2], value > 0 {
				result = "Yes"
				break
			}
		}
	}
	print(result)
}

twoStrings(s1: s1, s2: s2)

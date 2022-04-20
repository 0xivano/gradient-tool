# Dont be scammed for this gradient shit lool
# If you wa
def gradient(startrgb, endrgb, text: str):
	lenoft = len(text) 
	changer = int((int(endrgb[0]) - int(startrgb[0]))/lenoft)
	changeg = int((int(endrgb[0]) - int(startrgb[0]))/lenoft)
	changeb = int((int(endrgb[0]) - int(startrgb[0]))/lenoft)

	r = int(startrgb[0])
	g = int(startrgb[1])
	b = int(startrgb[2])
	dontskeedme = ""

	for letter in text:
		dontskeedme += (f"\x1b[38;2;{r};{g};{b}m{letter}")
		r+=changer
		g+=changeg
		b+=changeb
	return dontskeedme

print(gradient([132, 84, 211], [55, 191, 220], "Hello there this is a test of gradient tool."))

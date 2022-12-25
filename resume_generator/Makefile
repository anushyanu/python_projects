all:
	./generator.py --name xor --path . --author anushya --userlogic resume --begin begin
	./generator.py --name l3harris --path . --author neels --userlogic resume --begin begin

tex:
	cd xor_v1_00_a/cover_letter && pdflatex *.tex
	cd xor_v1_00_a/resume && pdflatex *.tex
	cd l3harris_v1_00_a/cover_letter && pdflatex *.tex
	cd l3harris_v1_00_a/resume && pdflatex *.tex


pdf:
	cd xor_v1_00_a/cover_letter && evince *.pdf
	cd xor_v1_00_a/resume && evince *.pdf
	cd l3harris_v1_00_a/cover_letter && evince *.pdf
	cd l3harris_v1_00_a/resume && evince *.pdf


clean:
	rm -rf xor*	

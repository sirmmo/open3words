
data/words.txt:
	mkdir -p data
	aspell -d en dump master | grep -E '^[a-z]{3,5}$$' >data/words.txt

clean:
	rm -rf data/words.txt

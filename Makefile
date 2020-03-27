
clean:
	rm -rf build/
	rm -rf dist/
	rm -f dungeon-dos.spec

linux:
	./release/release_linux.sh

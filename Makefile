
clean:
	rm -rf build/
	rm -rf dist/
	rm -f dungeon-dos.spec
	rm -rf dungeon-dos/

linux:
	./release/release_linux.sh

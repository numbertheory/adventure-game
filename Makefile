
clean:
	rm -rf build/
	rm -rf dist/
	rm -f dungeon-dos.spec
	rm -rf dungeon-dos/
	rm -f dungeon-dos-*.zip

linux:
	./release/release_linux.sh

mac:
	./release/release_mac.sh

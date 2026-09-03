def find_unused_files(db_file='db_referenced_files.txt', media_file='media_files.txt'):
	with open(db_file, 'r') as f:
		db_paths = set(f.read().splitlines())

	with open(media_file, 'r') as f:
		media_paths = set(f.read().splitlines())

	unused_files = media_paths - db_paths  # Files in media but not in db
	return unused_files

if __name__ == "__main__":
	unused = find_unused_files()
	with open('unused_files.txt', 'w') as f:
		for path in sorted(unused):
			f.write(f"{path}\n")
	print(f"Found {len(unused)} unused files. List saved to unused_files.txt")
from setuptools import setup, find_packages


with open('README.md') as file:
	description = file.read()


setup(
	name="armenian_latin_to_armenian_hy",
	version="0.0.1",
	description="Transliteration from Latin Armenian language to Armenian",
	packages=find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires=">=3.6",
	long_description=description,
	long_description_content_type="text/markdown"
)

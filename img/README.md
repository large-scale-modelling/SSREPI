# PURPOSE

This stores the images for the specification.

There are two versions of the images here, the mermaid, *.mmd is authoratative.

If you want to change the images, if there is a corresponding *.mmd file then please modify that.

```
mmdc -i "filename" -o "${basename filename}.png" -w 1000 -b white
 ```

# MANIFEST

+ `diagram-??.mmd` - The graphs of the schema and sub-schemas. If you want to change these, then please edit these.
+ `diagram-??.png` - The png corresponding to the mermaid diagrams. These are generated from the *.mmd files using `mmdc`. 
+ `dimensions_of_metadata.png` - The dimensions of metadata diagram. 
+ `README.md` - This file.
+ `render_diagrams.ps1` - convert all the mmd files to png files. This is a powershell script. 
+ `render_diagrams.sh` - convert all the mmd files to png files. This is a bash script.


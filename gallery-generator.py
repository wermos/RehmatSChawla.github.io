import subprocess


html_filename = "_pages/coffee_images.md"
gallery_dir = "assets/img/coffee"
html_text = '''---
layout: page
permalink: /coffee_images/
title: Coffee Photos
description: A collection of coffee photos - mostly ones I made, but some other especially pretty ones I drank too.
nav_order: 12
nav: false
---
'''

style_text = '''
<style>
    .photo-gallery {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
        grid-gap: 10px;
      }

      .photo-gallery img {
        width: 100%;
        height: auto;
        display: block;
        border-radius: 8px;
        box-shadow: 0 0 5px rgba(0, 0, 0, 0.3);
        transition: transform 0.3s ease-in-out;
      }

      .photo-gallery img:hover {
        transform: scale(1.05);
      }

      .bottom-left {
  position: absolute;
  bottom: 0px;
  left: 20px;
}
</style>

'''

html_text += style_text

def img_html(img_path, img_alt, style=1):
    if style == 0:
        return f'<img src="{img_path}" alt="{img_alt}">\n'
    elif style == 1:
        return f'''
      <div class="col">
            <div class="img-thumb">
              <img class="img-fluid" src="{img_path}" alt="{img_alt}">
              <div class="bottom-left"><a class="lightbox" href="{img_path}" style="color: white;">
                <i class="fa fa-plus"></i>
              </a></div>
          </div>
      </div>'''
    elif style == 2:
        return f'''
      <div class="col">
          <div class="img-thumb">
              {{% include figure.liquid path='{img_path}' title='{img_alt}' class='img-fluid' %}}
          </div>
      </div>'''
  # <i class="lni-plus"></i>

# read the file names
# ls_results = subprocess.check_output(f"ls {gallery_dir} -p").decode("utf-8").split("\n")
ls_results = subprocess.run(f"ls -p '{gallery_dir}'", shell=True, capture_output=True)
ls_output = ls_results.stdout.decode("utf-8")
ls_out_list = ls_output.split("\n")
# those that end with / are directories
file_names = [file_name for file_name in ls_out_list if not file_name.endswith("/")]
sub_dir_names = [file_name for file_name in ls_out_list if file_name.endswith("/")]
# remove the trailing /
sub_dir_names = [sub_dir_name[:-1] for sub_dir_name in sub_dir_names]
# keep the file names that end with .jpg, .jpeg or .png, or their capitalised versions
file_names = [file_name for file_name in file_names if file_name.endswith(".jpg") or file_name.endswith(".jpeg") or file_name.endswith(".png") or file_name.endswith(".JPG") or file_name.endswith(".JPEG") or file_name.endswith(".PNG")]

print("Files: ",file_names)


# sort the sub_dir_names
print("Directories (in order): ",sub_dir_names)

for sub_dir in sub_dir_names:
    # start a new section
    html_text += f'''<section id="about" class="section-padding">
      <div class="container">
        <div class="row">
          <div class="col-12">
            <div class="section-title-header text-center">
              <h1 class="section-title wow fadeInUp" data-wow-delay="0.2s">{sub_dir}</h1>
            </div>
          </div>
        </div>
      </div>
    '''
    # read the images inside the sub_dir
    sub_dir_path = gallery_dir + sub_dir + "/"
    # ls_results = subprocess.check_output(f"ls -p '{sub_dir_path}'").decode("utf-8").split("\n")
    subdir_ls_out_list = subprocess.run(f"ls -p '{sub_dir_path}'", shell=True, capture_output=True).stdout.decode("utf-8").split("\n")
    # those that end with / are directories
    file_names_sub_dir = [file_name for file_name in subdir_ls_out_list if not file_name.endswith("/")]
    # keep the file names that end with .jpg, .jpeg or .png
    file_names_sub_dir = [file_name for file_name in file_names_sub_dir if file_name.endswith(".jpg") or file_name.endswith(".jpeg") or file_name.endswith(".png") or file_name.endswith(".JPG") or file_name.endswith(".JPEG") or file_name.endswith(".PNG")]
    print(f"Files in sub dir {sub_dir}: ",file_names_sub_dir)

    html_text += '\n<div class="photo-gallery">\n'
    for file_name in file_names_sub_dir:
        html_text += img_html(sub_dir_path + "/" + file_name, file_name, style=2)
    html_text += '</div>\n'
    html_text += '</section>\n'

# now add the images that are not in any sub_dir
if len(file_names) > 0:
  section_header_present = True if len(sub_dir_names) != 0 else False
  section_header_text = '''<div class="container">
        <div class="row">
          <div class="col-12">
            <div class="section-title-header text-center">
              <h1 class="section-title wow fadeInUp" data-wow-delay="0.2s">Other Images</h1>
            </div>
          </div>
        </div>
      </div>
  '''
  html_text += f'''<section id="about" class="section-padding">
      {section_header_text if section_header_present else ""}
    <div class="photo-gallery">
    '''
  for file_name in file_names:
      html_text += img_html(gallery_dir + "/" + file_name, file_name, style=2)
  html_text += '</div>\n'
  html_text += '</section>\n'

# now for the end of the file
html_text += ''''''

with open(html_filename,"w") as f:
    f.write(html_text)

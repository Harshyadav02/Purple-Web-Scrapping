
import subprocess


bash_script_path = '/media/harsh/P/script/./crul.sh'        # path for the bash file

subprocess.run(['bash', bash_script_path])                    # running the bash file


#   Lists for holding the data 
name_data = []
data_pricing = []
rating_avg = []
total_rating = []
item_url = []
img_url = []
string = ""

#  opening the  file where the data is stored obtained by the crul file 
with open('data.txt', 'r') as file:


    inside_data_pricing = False
    current_data = ""
    inside_highlight_text_new = False

    for line in file:
        if '"highlight_text_new"' in line:
                inside_highlight_text_new = not inside_highlight_text_new
        if inside_highlight_text_new and ']' in line:
                inside_highlight_text_new = False
        if not inside_highlight_text_new and line.strip().startswith('"name"'):
                name_data.append(line.strip())
        
        if line.strip().startswith('"rating_avg"'):
                rating_avg.append(line.strip())
        if line.strip().startswith('"rating_count"'):
                total_rating.append(line.strip())
        if line.strip().startswith('"url"'):
                item_url.append(line.strip())
        if line.strip().startswith('"thumb_image_url"'):
                img_url.append(line.strip())
        if inside_data_pricing:
                
            if '},' in line:
                    inside_data_pricing = False
                    string += current_data.strip()+"\n"
                    string += '}'
                    current_data = ""
                    
            else:
                current_data += line.strip()+"\n"

        elif line.strip().startswith('"data_pricing"'):
            inside_data_pricing = True

              


data_pricing = string.split("}")
data_pricing = [substring.strip() for substring in data_pricing]

#  writting the data back to the file in a readble formate 
with open('Men/data.txt' ,'a') as file2:

        length = 0 

        for name_data, rating_avg  ,total_rating,img_url in zip(name_data , rating_avg,total_rating,img_url):
                file2.write(f"{name_data}\n{rating_avg}\n{total_rating}\n{img_url}\n")
            
                while(length < len(data_pricing)):
                  
                        file2.write(data_pricing[length].strip().strip())

                        length +=1
                        file2.write("\n\n") 
                        break
            




      











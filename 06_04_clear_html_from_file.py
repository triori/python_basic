def delete_html_tags(html_file, result_file='cleaned.txt'): 
      with open(html_file, 'r', encoding='utf-8') as file_in: 
           with open(result_file, 'w', encoding='utf-8') as file_out:
                in_tag = False
                for line in file_in:
                     cleaned_line = ''
                     for char in line:
                          if char == '<':
                               in_tag = True
                          elif char == '>':
                               in_tag = False
                          elif not in_tag:
                               cleaned_line += char
                     
                     if cleaned_line.strip():
                          file_out.write(cleaned_line)

delete_html_tags('draft.html', 'cleaned.txt')

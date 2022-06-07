read_file = open('example.txt');
old_content = ''

for line in read_file:
    old_content += line

read_file.close()

new_content = old_content.replace('placement', 'screening')

write_file = open('example.txt', 'w')
write_file.write(new_content)
write_file.close()

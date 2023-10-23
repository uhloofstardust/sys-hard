import json
import tkinter as tk

rules_conf_file = '/etc/usbguard/rules.conf'
rules_conf_file = './sample.txt'

lines_list = []

try:
    with open(rules_conf_file, 'r') as file:
        for line in file:
            lines_list.append(line.strip())

except FileNotFoundError:
    print(f"File not found: {rules_conf_file}")
except Exception as e:
    print(f"An error occurred: {e}")

objects = []

for line in lines_list:
    if line != "":
        temp_list = line.split('"')
        temp_0 = temp_list[0]
        temp_0_split = temp_0.split(' ')
        temp_dict = {}
        temp_dict["status"] = temp_0_split[0]
        temp_dict["id"] = temp_0_split[2]
        temp_dict["serial"] = temp_list[1]
        temp_dict["name"] = temp_list[3]
        objects.append(temp_dict)



def change_rule_status(id_to_block):

    with open(rules_conf_file, 'r') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        if id_to_block in line:
            if "allow" in line:
                lines[i] = line.replace("allow", "block")
            elif "block" in line:
                lines[i] = line.replace("block", "allow")

    with open(rules_conf_file, 'w') as file:
        file.writelines(lines)




def update_status(index, new_status):
    update_display()
    change_rule_status(objects[index]["id"])
    objects[index]["status"] = new_status
    update_display()




root = tk.Tk()
root.title("USB")

frame = tk.Frame(root)
frame.pack()

circle_labels = []

for index, obj in enumerate(objects):
    circle = tk.Label(frame, text="●", font=("Arial", 12), width=2, anchor="w")
    circle.grid(row=index, column=0, padx=10, pady=5)
    circle_labels.append(circle)

    label = tk.Label(frame, text=f"ID: {obj['id']}, Name: {obj['name']}")
    label.grid(row=index, column=1, padx=10, pady=5)

    allow_button = tk.Button(frame, text="Allow", command=lambda i=index: update_status(i, "allow"))
    allow_button.grid(row=index, column=2, padx=5, pady=5)

    block_button = tk.Button(frame, text="Block", command=lambda i=index: update_status(i, "block"))
    block_button.grid(row=index, column=3, padx=5, pady=5)


def update_display():
    for i, obj in enumerate(objects):
        if obj["status"] == "block":
            circle_labels[i].config(fg="red")
        else:
            circle_labels[i].config(fg="green")

update_button = tk.Button(root, text="refresh", command=update_display)
update_button.pack()
update_display()
root.mainloop()


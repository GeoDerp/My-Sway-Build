#Toggle between output sinks 
#Author GeoDerp
#License MIT  
import subprocess

def get_current_sink_id():
    id = int(subprocess.getoutput("wpctl status -n | grep -zoP '(?<=Sinks:)(?s).*?(?=├─)' | sed -n 's/│  //p' | sed -n 's/*   //p'").split()[0].replace('.', ''))
    return id

# Get a list of all sinks  
# wpctl command inspired by https://github.com/logon84/Pipewire-sound-sink-switcher
def get_sink_list():
    result = subprocess.getoutput("wpctl status -n | grep -zoP '(?<=Sinks:)(?s).*?(?=├─)' | sed -n 's/ │  //p'")
    sink_dict = {}

    for line in result.splitlines():
        temp = line.replace('*', '').split()
        if temp:
            sink_dict[int(temp[0].replace('.', ''))] = temp[1]
    
    return sink_dict         

# Get dict of available sinks
sink_dict = get_sink_list()
# Get get current default sink id
sink_default = get_current_sink_id()
# Get get a list of all sink ids (to iterate)
sink_ids = list(sink_dict.keys())
# find the index of the current default sink id in list 
default_index =  sink_ids.index(sink_default)

#loop through ids until wpctl successfully sets new sink to default
while sink_default is get_current_sink_id() or default_index > 1000:
    if default_index < len(sink_ids) - 1:
        next_sink = sink_ids[default_index + 1]
    else:
        next_sink = sink_ids[0]
    return_code = subprocess.call("wpctl set-default " + str(next_sink), shell=True)
    if not bool(return_code):
        default_index += 1
    else: quit()

print("Sink set to: " + str(next_sink) + " : " + sink_dict[next_sink])




import sys
import os

# Input Setting
ff_type=sys.argv[1]
temperature=int(sys.argv[2])
h_name="./"+ff_type+"/enthalpy.out"
ts_name="./"+ff_type+"/entropy.out"
h_file=open(h_name,'r')
ts_file=open(ts_name,'r')
os.mkdir("./results")
output_name = "./results/"+ff_type+"_%1.f.table" % (temperature)
output_file=open(output_name,'w')

# Variables
r=[]
h=[]
ts=[]
f_h=[]
f_ts=[]
str_header=""

# Linear extrapolation
i=0
for line1 in h_file:
    if i>=5:
        line1_e = line1.split()
        r.append(float(line1_e[1]))
        h.append(float(line1_e[2]))
        f_h.append(float(line1_e[3]))
    else:
        str_header += line1
    i+=1

j=0
for line2 in ts_file:
    if j>=5:
        line2_e=line2.split()
        ts.append(float(line2_e[2]))
        f_ts.append(float(line2_e[3]))
    j+=1

# Output
# Header for LAMMPS table
output_file.write(str_header)
# Table contents
for i in range(0,len(r)):
    corrected_e=h[i]+ts[i]/1000.0*float(temperature)
    corrected_f=f_h[i]+f_ts[i]/1000.0*float(temperature)
    str_out = "%d %.6f %.6f %.6f\n" % (i+1, r[i], corrected_e, corrected_f)
    output_file.write(str_out)

h_file.close()
ts_file.close()
output_file.close()

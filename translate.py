from string import maketrans

in_tab="abcdefghijklmnopqrstuvwxyz"
out_tab="cdefghijklmnopqrstuvwxyzab"
tran_tab=maketrans(in_tab,out_tab)

str="g fmnc wms bgblr rpylqjyrc grzw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."  
print(str.translate(tran_tab))

  

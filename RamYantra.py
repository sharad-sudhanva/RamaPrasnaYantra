next = 9
delimiter = 15 



def result(pos_res):

    if pos_res in [0,1,5,6,8]:
        print("Success")
    elif pos_res in [2,3,7]:
        print("Failure")
    else:
        print("Doubtful")

def compare(res_str,postulates):
    res_str = res_str.split()
    res_str.sort()
    for i in range(len(postulates)):
        temp = sorted(postulates[i].split())
          
        if temp == res_str:
            return i

def compute(row,col,array):
    res_str = array[row][col]
    t_r,t_c = row,col

    col = (col+next)
    if col >= delimiter:
        row = row+1
        col = col - delimiter
    if row == delimiter:
        row = 0

    while not (t_r == row and t_c == col):
        #print(array[row][col])
        if array[row][col].isupper():
            res_str = res_str + (array[row][col])
            
        else:
            res_str = res_str + " " + (array[row][col])
        col = (col+next)
        if col >= delimiter:
            row = row+1
            col = col -delimiter
        if row ==delimiter:
            row = 0
         
    return res_str

array = [
    ['su', 'pra', 'u', 'bi', 'hoo', 'mu','ga','ba','su','nu','bi','gha','dhi','e','da'],
    ['ra','ru','pha','si','si','rahi','basa','hi','mam','la','na','la','ya','na','am'],
    ['suja','soo','ga','su','ku','ma','sa','ga','tha','na','e','la','dhaa','bae','noo'],
    ['tya','ra','na','ku','joo','ma','ri','ra','ra','a','kii','hoo','sam','raa','ya'],
    ['pu','su','thha','sii','jae','e','ga','ma','sam','ka','rae','hoo','sa','pa','ni'],
    ['tha','ra','tha','ra','sa','hu','ha','ba','ba','pa','chi','sa','hi','sa','thu'],
    ['ma','kaa','A','ra','ra','ma','mi','mii','mha','A','jaa','hoo','hii','A','A'],
    ['thaa','raa','raee','rii','hru','kaa','pha','khaa','juu','eee','ra','raa','pu','da','la'],
    ['ni','koo','joo','goo','na','mu','ji','ya','nee','mani','ka','ja','pa','sa','la'],
    ['hi','raa','mi','sa','ri','ga','da','nmu','kha','ma','khi','ji','ma','tha','jam'],
    ['sim','kha','nu','na','koo','mi','nija','rka','ga','dhu','dha','su','kaa','sa','ra'],
    ['gu','ba','ma','a','ri','ni','ma','la','A','na','ddha','thi','na','ka','bha'],
    ['naa','pu','va','a','A','ra','la','A','aee','thu','ra','na','nu','vyi','tha'],
    ['si','hu','su','mha','raa','ra','sa','sa','ra','tha','na','kha','A','ja','A'],
    ['ra','A','A','laa','dhii','A','rii','A','hoo','hii','khaa','joo','ee','raa','ree']
]

postulates = [
    "su nu si ya sa tya a sii sa ha maA rii pu ji hi ma na kaa ma naa thu mhaA rii",
    "pra bi si na ga ra kii jae pa ba kaa jaa hru da ya raa khi koo sa la pu ra raa jaA",
    "u gha rahi am tha na hoo e ni baA hoo kaa la nee mi ji mi raA va na raA hoo",
    "bi dhi basa suja na ku sam ga tha pa ra hii pha ni mani sa ma nija gu na a nu sa ra hii",
    "hoo e hi soo e joo raa ma ra chi raA khaa koo ka ri tha rka ba ddhaA vyi saA khaa",
    "mu da mam ga la ma ya sam tha sa maA juu joo ja ga jam ga ma thi ra tha raA joo",
    "ga ra la su dhaa ri pu ka ra hi mi thaa eee goo pa da sim dhu a na la si tha laa ee",
    "ba ru na ku bae ra su rae sa sa mii raa ra na sa nmu kha dha ri kaA hu na dhii raa",
    "su pha la ma noo ra thha hoo hu thu mha raee raa mu la kha nu su ni bha aee su khaA ree"
]

x = int(input())
y = int(input())
res_str = compute(x,y,array)
pos_res = compare(res_str,postulates)
result(pos_res)


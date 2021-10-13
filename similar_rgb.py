class Sol:
    def similar_rgb(self,col):
        res=["#"]
        list = ['00', '11', '22', '33', '44', '55', '66', '77', '88', '99', 'aa', 'bb', 'cc', 'dd', 'ee', 'ff']
        for i in range(1,6,2):
            dif=[]
            for j in list:
                dif.append(abs(int(col[i:i+2],16)-int(j,16)))
                minpos = dif.index(min(dif))
            res.append(str(list[minpos]))
        return "".join(res)

if __name__ == '__main__':
    p=Sol()
    print(p.similar_rgb(col='#09bbcc'))

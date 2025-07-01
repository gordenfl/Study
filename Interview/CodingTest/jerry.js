/*
We are looking for a program that manages “intensity” by segments. Segments are intervals from -infinity to infinity, we liked you to implement functions that updates intensity by an integer amount for a given range. All intensity starts with 0. Please implement these two functions:
● add(from, to, amount)
● set(from, to, amount)
Here is an example sequence (data stored as an array of start point and value for each segment.):
Start: []
Call: add(10, 30, 1) => [[10,1],[30,0]]
Call: add(20, 40, 1) => [[10,1],[20,2],[30,1],[40,0]]
Call: add(10, 40, -2) => [[10,-1],[20,0],[30,-1],[40,0]]
Start: []
Call: add(10, 30, 1) => [[10,1],[30,0]]
Call: add(20, 40, 1) => [[10,1],[20,2],[30,1],[40,0]]
Call: add(10, 40, -1) => [[20,1][30, 0]]
Call:add(10,40,-1) = > [[10,-1],[20,0],[30,-1],[40,0]]
*/

 class IntensityMgr {
    constructor() {
        this.points = []
        this.values = []
    }

    p_getPointIndex(x) {
        let l = 0, r = this.points.length
        while(l < r) {
            let m = Math.floor((l + r) / 2)
            if (this.points[m] <= x) {
                l = m + 1
            } else {
                r = m 
            }
        }
        return l - 1
    }

    p_CheckIndexValue(x) {
        if (this.points.includes(x)) {
            return
        }

        //x does not exist, I will try to add x into points and add value with i-1
        let i = this.p_getPointIndex(x);
        let v = i >= 0 ? this.values[i] : 0
        this.points.splice(i+1, 0, x)
        this.values.splice(i+1, 0, v)
    }

    p_cleanUpData() {
        let newP = []
        let newV = []

        let lastVal = null;
        let flag = false;
        for(let i = 0; i < this.points.length; ++i) {
            if (this.values[i] == lastVal) {
                continue
            }
            if(this.values[i]!=0) {
                flag = true
            }
            if (flag == true) {
                newP.push(this.points[i])
                newV.push(this.values[i])
                lastVal = this.values[i]
            }
        }
        this.points = newP
        this.values = newV
    }

    add(from, to, amount) {
        if (undefined == from || undefined == to || undefined == amount) {
            return
        }
        this.p_CheckIndexValue(from)
        this.p_CheckIndexValue(to)

        for (let i = 0; i < this.points.length; ++i) {
            let x = this.points[i]
            if (x >= to) 
                break
            if (x >= from) 
                this.values[i] += amount
        }
        this.p_cleanUpData()
    }

    set(from, to, amount) {
        if (undefined == from || undefined == to || undefined == amount) {
            return
        }

        this.p_CheckIndexValue(from)
        this.p_CheckIndexValue(to)

        let newP = []
        let newV = []

        for (let i = 0; i < this.points.length; ++i) {
            let x = this.points[i]
            let v = this.values[i]
            if (x >= from && x < to) {
                continue
            }
            newP.push(x)
            newV.push(v)
        }

        newP.push(from)
        newV.push(amount)

        let idx = this._findIndex(to)
        let afterVal = idx >= 0 ? this.values[idx] : 0
        newP.push(to)
        newV.push(afterVal)

        this.points = newP
        this.values = newV
        this.p_cleanUpData()
    }

    showData() {
        console.log(this.points.map((p, i) => [p, this.values[i]]))
    }
 }

 const sm = new IntensityMgr()

 sm.add(10, 30, 1)
 sm.showData()
 sm.add(20, 40, 1)
 sm.showData()
 sm.add(10, 40, -2)
 sm.showData()
 sm.add(15, 35, 5)
 sm.showData()

 console.log("=========================")

 const sm1 = new IntensityMgr()
 sm1.add(10, 30, 1)
 sm1.showData()
 sm1.add(20, 40, 1)
 sm1.showData()
 sm1.add(10, 40, -1)
 sm1.showData()
 sm1.add(10, 40, -1)
 sm1.showData()
 
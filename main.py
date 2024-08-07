import array
import numpy as np

class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n=len(grid)
        for i,liste in enumerate(grid):
            if liste.count(1)==n-1:
                return i



class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        dictionnaire={'P':-1, 'G':-1, 'M':-1}
        paper=0
        metal=0
        glass=0
        for i,s in enumerate(garbage):
            if 'P' in s:
                paper+=s.count('P')
                dictionnaire['P']=i
            if 'G' in s:
                glass+=s.count('G')
                dictionnaire['G']=i
            if 'M' in s:
                metal+=s.count('M')
                dictionnaire['M']=i
        somme=paper+glass+metal
        for key in dictionnaire:
            if dictionnaire[key]!=-1:
                for j in range(dictionnaire[key]):
                    somme+=travel[j]
        return somme
    


class Solution:
    def minOperations(self, n: int) -> int:
        arr=[0]*n
        for i in range(n):
            arr[i]=2*i+1
        if n%2!=0:
            somme=0
            for i in range(n//2):
                somme+=arr[n//2]-arr[i]
            return somme
        else:
            somme=1
            arr[n//2]=arr[n//2 - 1]+1
            arr[n//2 - 1]=arr[n//2]
            for i in range(n//2):
                somme+=arr[n//2]-arr[i]
            return somme



class Solution:
    def first_positive_index(self, nums:List[int])->int:
        left=0
        right=len(nums)-1
        while left<=right:
            middle=(left+right)//2
            if nums[middle]<=0:
                left=middle+1
            else:
                right=middle-1
        return left

    def last_negative_index(self, nums:List[int]) ->int:
        left=0
        right=len(nums)-1
        while left<=right:
            middle=(left+right)//2
            if nums[middle]<0:
                left=middle+1
            else:
                right=middle-1
        return right

    def maximumCount(self, nums: List[int]) -> int:
        positive_index=self.first_positive_index(nums)
        negative_index=self.last_negative_index(nums)
        pos=len(nums)-positive_index
        neg=negative_index+1
        return max(pos,neg)
    


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        while left<=right:
            middle=(left+right)//2
            if nums[middle]==target:
                return middle
            elif nums[middle]<target:
                left=middle+1
            else:
                right=middle-1
        return -1
    

#Erreur de code pcq j'update a chaque fois copy_list. Peu efficace mais l'idee est la
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        copy_list=list(arr)
        n=len(arr)
        i=0
        while i<n:
            if arr[i]==0 and i+2<n:
                arr[i+1]=0
                for j in range(i+2,n):
                    arr[j]=copy_list[j-1]
                i+=2
                copy_list=list(arr)
            if arr[i]==0 and i+2>=n:
                arr[i+1]=0
            else:
                i+=1

#Version corrigee
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n=len(arr)
        result=[]
        for num in arr:
            if num!=0:
                result.append(num)
            if num==0:
                result.append(num)
                if len(result)<n:
                    result.append(0)
            if len(result)>=n:
                break
        for i in range(n):
            arr[i]=result[i]



class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        occurence=defaultdict(int)
        a=0
        b=0
        for liste in grid:
            for element in liste:
                occurence[element]+=1
        for i in range(1,(len(grid[0]))**2 + 1):
            if i not in occurence:
                b=i
                break
        a=max(occurence, key=occurence.get)
        return [a,b]
    


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        indices=defaultdict(list)
        if k==0:
            if 0 in nums:
                return False
            return True
        for i,num in enumerate(nums):
            indices[num].append(i)
        liste=indices[1]
        n=len(liste)
        for i in range(n):
            for j in range(n):
                if i!=j and abs(liste[i]-liste[j])-1<k:
                    return False
        return True
    





class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output=[]
        x=map(list,itertools.permutations(nums))
        return list(x)
    

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        n=len(nums)
        indices=defaultdict(list)
        for i,num in enumerate(nums):
            indices[num].append(i)
        liste_indices=[]
        for j in range(1,k+1):
            liste_indices.append(max(indices[j]))
        return n-min(liste_indices)
    


class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        if len(set(target))!=len(target):
            dict_s=defaultdict(int)
            dict_target=defaultdict(int)
            for char in s:
                dict_s[char]+=1
            for char in target:
                dict_target[char]+=1
            liste=[]
            for char in target:
                liste.append(dict_s[char]//dict_target[char])
            return min(liste)
        liste_occurence=[]
        for char in target:
            liste_occurence.append(s.count(char))
        return min(liste_occurence)



class Solution:
    def largestDigit(self,num:int) -> int:
        s=str(num)
        maximum=0
        for char in s:
            maximum=max(maximum, int(char))
        return maximum

    def maximumSum(self,nums:List[int])->int:
        n=len(nums)
        if nums==[]:
            return 0
        maximum=0
        for i in range(n):
            for j in range(n):
                if j!=i:
                    maximum=max(maximum,nums[i]+nums[j])
        return maximum


    def maxSum(self, nums: List[int]) -> int:
        max_digit=defaultdict(list)
        for num in nums:
            largest_digit_num=self.largestDigit(num)
            max_digit[largest_digit_num].append(num)
        liste_somme=[]
        for liste in max_digit.values():
            if len(liste)>1:
                liste_somme.append(self.maximumSum(liste))
        if liste_somme==[]:
            return -1
        return max(liste_somme)
    

class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count_s=Counter(s)
        count_t=Counter(t)
        steps=0
        for char in count_s:
            if char in count_t:
                steps+=max(0,count_s[char]-count_t[char])
            else:
                steps+=count_s[char]
        return steps
    


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        mot1=sorted(list(set(word1)))
        mot2=sorted(list(set(word2)))
        if mot1!=mot2:
            return False  
        occurence1=defaultdict(int)
        occurence2=defaultdict(int)
        for char in word1:
            occurence1[char]+=1
        for char in word2:
            occurence2[char]+=1
        liste1=sorted(list(occurence1.values()))
        liste2=sorted(list(occurence2.values()))
        return liste1==liste2
    


#Erreur Buddy Strings je me suis casse le cerveau
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        if len(goal)==len(s)==1:
            return False
        mot1=sorted(list(set(s)))
        mot2=sorted(list(set(goal)))
        if mot1!=mot2:
            return False
        indices_s=defaultdict(list)
        indices_goal=defaultdict(list)
        for i,char in enumerate(s):
            indices_s[char].append(i)
        for i,char in enumerate(goal):
            indices_goal[char].append(i)
        if s!=goal:
            count=0
            for char in s:
                if indices_s[char]!=indices_goal[char]:
                    count+=1
            return count==2
        if s==goal:
            if len(list(set(s)))==1:
                return True
            numbers = [x for x in range(2,10)]
            lengths = [len(liste) for liste in indices_s.values()]
            intersection = set(numbers) & set(lengths)
            if intersection:
                return True
            else:
                return False
            
#Correction
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        if s==goal:
            seen=set()
            for char in s:
                if char in seen:
                    return True
                seen.add(char)
            return False
        if s!=goal:
            n=len(s)
            liste=[]
            for i in range(n):
                if s[i]!=goal[i]:
                    liste.append(i)
            if len(liste)==2 and s[liste[0]]==goal[liste[1]] and s[liste[1]]==goal[liste[0]]:
                return True
            return False
        



class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1==s2:
            return True
        diff=[]
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                diff.append(i)
        if len(diff)==2 and s1[diff[0]]==s2[diff[1]] and s1[diff[1]]==s2[diff[0]]:
            return True
        return False
    


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        restaurant=defaultdict(list)
        for i,string in enumerate(list1):
            if string in list2:
                restaurant[string].append(i)
                restaurant[string].append(list2.index(string))
        output=[]
        minimum=min([sum(liste) for liste in restaurant.values()])
        for key,val in restaurant.items():
            if sum(val)==minimum:
                output.append(key)
        return output


class Solution:
    def secondHighest(self, s: str) -> int:
        numbers=[int(char) for char in s if char.isdigit()]
        if len(list(set(numbers)))<2:
            return -1
        unique_numbers=list(set(numbers))
        liste_triee=sorted(unique_numbers, reverse=True)
        return liste_triee[1]
    
    
class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        occurence=defaultdict(list)
        for i,char in enumerate(number):
            occurence[char].append(i)
        elu=0
        liste_indice=occurence[digit]
        for i in liste_indice:
            candidat=int(number[:i]+number[i+1:])
            elu=max(elu,candidat)
        return str(elu)
    

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        occurence=defaultdict(int)
        for char in s:
            occurence[char]+=1
        return len(list(set(occurence.values())))==1
    


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        frequency=defaultdict(int)
        for num in nums:
            frequency[num]+=1
        m=max(list(frequency.values()))
        liste_num=[]
        for key,val in frequency.items():
            if val==m:
                liste_num.append(key)
        somme=0
        for num in liste_num:
            somme+=nums.count(num)
        return somme
    


class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        n=len(nums1)
        m=len(nums2)
        pair=0
        for i in range(n):
            for j in range(m):
                if nums1[i]%(nums2[j]*k)==0:
                    pair+=1
        return pair



class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        n=len(nums)
        pair=0
        for i in range(n):
            for j in range(i+1,n):
                if abs(nums[i]-nums[j])==k:
                    pair+=1
        return pair


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        n=len(nums)
        pair=0
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]==nums[j] and (i*j)%k==0:
                    pair+=1
        return pair
    


class Solution:
    def sumDigit(self,n:int)->int:
        somme=0
        for char in str(n):
            somme+=int(char)
        return somme 

    def countLargestGroup(self, n: int) -> int:
        occurence=defaultdict(int)
        for number in range(1,n+1):
            sum_number=self.sumDigit(number)
            occurence[sum_number]+=1
        max_values=max(occurence.values())
        return len([key for key,val in occurence.items() if val==max_values])
    


class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        seen=set()
        n=len(word)
        i=0
        while i<n:
            if word[i].isdigit():
                number=word[i]
                while i+1<n and word[i+1].isdigit():
                    number+=word[i+1]
                    i+=1
                seen.add(int(number))
            i+=1
        return len(seen)
    


class Solution:
    def commonLetters(self, word1:str,word2:str)->bool:
        for char in word1:
            if char in word2:
                return False
        return True 

    def maxProduct(self, words: List[str]) -> int:
        maximum=0
        for i,word in enumerate(words):
            for j in range(i+1,len(words)):
                if self.commonLetters(word,words[j]):
                    maximum=max(maximum,len(word)*len(words[j]))
        return maximum
    


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n=len(arr)
        left=0
        right=n-1
        while left<=right:
            middle=(left+right)//2
            if arr[middle+1]-arr[middle]>=0:
                left=middle+1
            else:
                right=middle-1
        return left
    

class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num+2*t
    

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if not [num for num in nums if num%3!=0]:
            return 0
        somme=0
        for i in range(len(nums)):
            if nums[i]%3==2:
                somme+=1
            else:
                somme+=nums[i]%3
        return somme
    

class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        string=str(num)
        potentielle=[]
        beauty=0
        for i in range(len(string)-k+1):
            potentielle.append(int(string[i:i+k]))
        for candidat in potentielle:
            if candidat!=0 and num%candidat==0:
                beauty+=1
        return beauty
    

class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        if n==1:
            return 0
        position=0
        direction=1
        for _ in range(k):
            position+=direction
            if position==0 or position==n-1:
                direction*=-1
        return position
    


class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        position=1
        direction=1
        for _ in range(time):
            position+=direction
            if position==1 or position==n:
                direction*=-1
        return position
    


class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        if purchaseAmount%10==0:
            return 100-purchaseAmount
        basis=(purchaseAmount//10)*10
        if purchaseAmount%10>=5:
            basis+=10
        return 100-basis
    


class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        count=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if gcd(int(str(nums[i])[0]),int(str(nums[j])[-1]))==1:
                    count+=1
        return count
    



class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count=0
        for integer in range(low,high+1):
            x=str(integer)
            if len(x)%2==0:
                n=len(x)//2
                first_half=[int(x[i]) for i in range(0,n)]
                second_half=[int(x[i]) for i in range(n,len(x))]
                if sum(first_half)==sum(second_half):
                    count+=1
        return count
    


class Solution:
    def sumDigit(self, n:int)->int:
        string=str(n)
        n=len(string)
        somme=0
        for i in range(n):
            somme+=int(string[i])
        return somme 

    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        dictionnaire={i:0 for i in range(1,46)}
        for number in range(lowLimit, highLimit+1):
            sum_number=self.sumDigit(number)
            dictionnaire[sum_number]+=1
        return max(list(dictionnaire.values()))
    


class Solution:
    def countTriples(self, n: int) -> int:
        count=0
        for a in range(1,n):
            for b in range(1,n):
                x=a*a+b*b
                racine=int(sqrt(x))
                if racine*racine==x and racine<=n:
                    count+=1
        return count
    


class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        x=min(numOnes,k)      
        restant1=max(0,k-x) 
        y=min(numZeros,restant1)
        restant2=max(0,restant1-y)
        max_sum=x+restant2*(-1)
        return max_sum 
    


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        liste=sorted(nums)
        n=len(nums)
        counting={'positif':0, 'negatif':0}
        for num in nums:
            if num>=0:
                counting['positif']+=1
            counting['negatif']+=1
        if counting['negatif']==0 or counting['positif']==0:
            return liste[n-1]*liste[n-2]*liste[n-3]
        candidat1=liste[n-1]*liste[n-2]*liste[n-3]
        candidat2=liste[0]*liste[1]*liste[-1]
        return max(candidat1,candidat2)
    


class Solution:
    def gcd(self,a:int,b:int)->int:
        while b>0:
            a,b=b,a%b
        return a
    
    def divisor(self,n:int)->int:
        divisors=[]
        for i in range(1,n+1):
            if n%i==0:
                divisors.append(i)
        return divisors
        
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1=len(str1)
        len2=len(str2)
        gcd_length=self.gcd(len1,len2)
        divisors=sorted(self.divisor(gcd_length), reverse=True)
        for d in divisors:
            candidat=str1[:d]
            if candidat*(len1//d)==str1 and candidat*(len2//d)==str2:
                return candidat
        return ""
    


#Premiere version nzive ---> Time Limit
class Solution:
    def isMonotone(self,n:int)->bool:
        number=str(n)
        length=len(number)
        i=0
        while i<length-1:
            if int(number[i+1])<int(number[i]):
                return False
            i+=1
        return True

    def monotoneIncreasingDigits(self, n: int) -> int:
        for i in range(n,-1,-1):
            if self.isMonotone(i):
                return i
            

#Deuxieme version
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        number=list(str(n))
        length=len(number)
        mark=length
        for i in range(length-1):
            if int(number[i])>int(number[i+1]):
                mark=i
                break
        if mark==length:
            return n
        while mark>0 and number[mark]==number[mark-1]:
            mark-=1
        number[mark]=str(int(number[mark])-1)
        for i in range(mark+1,length):
            number[i]='9'
        return int("".join(number))



class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        number=min(x,y//4)
        if number%2!=0:
            return "Alice"
        return "Bob"
    

class Solution:
    def numberOfCuts(self, n: int) -> int:
        if n==1:
            return 0
        if n%2==0:
            return n//2
        return n
    

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        string1=list(reversed(a))
        string2=list(reversed(b))
        somme1=0
        somme2=0
        for i in range(len(string1)):
            somme1+=int(string1[i])*(2**i)
        for i in range(len(string2)):
            somme2+=int(string2[i])*(2**i)
        somme=somme1+somme2
        return bin(somme)[2:]
    



class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        liste_sortie=[]
        list_words=sentence.split()
        for i,word in enumerate(list_words):
            if word[0].lower() in ['a','e','i','o','u']:
                liste_sortie.append(word+'ma'+'a'*(i+1))
            else:
                word=word[1:] + word[0]
                liste_sortie.append(word+'ma'+'a'*(i+1))
        return ' '.join(liste_sortie)
    


class Solution:
    def diviseurs(self,num:int)-> list:
        liste_diviseurs=[]
        for i in range(1,num//2+1):
            if num%i==0:
                liste_diviseurs.append(i)
        return liste_diviseurs

    def checkPerfectNumber(self, num: int) -> bool:
        if num%2!=0:
            return False
        return sum(self.diviseurs(num))==num
    

#Dans la base n-2, n=1x(n-2)^1 + 2x(n-2)^0 donc sa representation dans la base n-2 est 12. 1é n'est pas un palindrome
class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        return False
    

class Solution:
    def reverseInteger(self,n:int)->int:
        string=str(n)
        reversed_string=string[::-1]
        return int(reversed_string)

    def countDistinctIntegers(self, nums: List[int]) -> int:
        liste_reversed=[0]*len(nums)
        for i,number in enumerate(nums):
            liste_reversed[i]=self.reverseInteger(number)
        liste_sortie=nums + liste_reversed
        return len(set(liste_sortie))
    


class Solution:
    def reverse(self, x: int) -> int:
        string=str(abs(x))
        reversed_string=string[::-1]
        reversed_int=int(reversed_string)
        if not -(2**31)<=reversed_int<=2**31-1:
            return 0
        if x>=0:
            return reversed_int
        else:
            return -reversed_int
        



class Solution:
    def reversal(self,num:int)->int:
        string=str(num)
        reversed_string=string[::-1]
        reversed_integer=int(reversed_string)
        return reversed_integer

    def isSameAfterReversals(self, num: int) -> bool:
        first_reversed=self.reversal(num)
        second_reversed=self.reversal(first_reversed)
        return num==second_reversed
    


class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        count=0
        for i in range(len(words)-1):
            for j in range(i+1,len(words)):
                if words[i]==words[j][::-1]:
                    count+=1
        return count
    


class Solution:
    def manipulation(self,nums:List[int])->list:
        liste_sortie=[0]*(len(nums)-1)
        for i in range(len(nums)-1):
            liste_sortie[i]=(nums[i]+nums[i+1])%10
        return liste_sortie

    def triangularSum(self, nums: List[int]) -> int:
        while len(nums)>1:
            nums=self.manipulation(nums)
        return nums[0]
    


class Solution:
    def round(self,s:str,k:int)->str:
        n=len(s)
        first_list=[]
        i=0
        while i<len(s):
            first_list.append(s[i:i+k])
            i+=k
        second_list=[0]*len(first_list)
        for i,element in enumerate(first_list):
            second_list[i]=sum([int(char) for char in element])
        sortie=str()
        for i in range(len(second_list)):
            sortie=sortie + str(second_list[i])
        return sortie

    def digitSum(self, s: str, k: int) -> str:
        if len(s)>k:
            sortie=self.round(s,k)
        while len(s)>k:
            s=self.round(s,k)
        return s
    



class Solution:
    def operation(self,nums:List[int])->List[int]:
        n=len(nums)
        newNums=[0]*(n//2)
        for i in range(n//2):
            if i%2==0:
                newNums[i]=min(nums[2*i],nums[2*i+1])
            else:
                newNums[i]=max(nums[2*i],nums[2*i+1])
        return newNums

    def minMaxGame(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        while len(nums)>1:
            nums=self.operation(nums)
        return nums[0]
        



    class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        n=len(mountain)
        liste_sortie=[]
        for i in range(1,n-1):
            if mountain[i]>mountain[i-1] and mountain[i]>mountain[i+1]:
                liste_sortie.append(i)
        return liste_sortie
    


class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        dictionnaire=defaultdict(int)
        for liste in items1:
            dictionnaire[liste[0]]+=liste[1]
        for liste in items2:
            dictionnaire[liste[0]]+=liste[1]
        liste_sortie=[[key,val] for key,val in dictionnaire.items()]
        return sorted(liste_sortie,key=lambda x:x[0])
    


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        dictionnaire=defaultdict(int)
        for liste in nums1:
            dictionnaire[liste[0]]+=liste[1]
        for liste in nums2:
            dictionnaire[liste[0]]+=liste[1]
        sortie=[[key,val] for key,val in dictionnaire.items()]
        return sorted(sortie, key=lambda x:x[0])
    


class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        students=0
        n=len(startTime)
        for i in range(n):
            if startTime[i]<=queryTime and endTime[i]>=queryTime:
                students+=1
        return students
    


class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        dictionnaire=defaultdict(int)
        for i,liste in enumerate(mat):
            dictionnaire[i]=liste.count(1)
        max_value=max(list(dictionnaire.values()))
        liste_keys=[key for key,val in dictionnaire.items() if val==max_value]
        key=min(liste_keys)
        return [key,dictionnaire[key]]
    


class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        seen=set()
        for liste in nums:
            beginning=liste[0]
            end=liste[1]
            for i in range(beginning,end+1):
                seen.add(i)
        return len(seen)
    


class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        current_capacity=capacity
        steps=0
        n=len(plants)
        for i in range(n):
            if current_capacity>=plants[i]:
                steps+=1
                current_capacity-=plants[i]
            else:
                steps+=2*i
                current_capacity=capacity-plants[i]
                steps+=1
        return steps
    


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        gagnants=set()
        perdants=set()
        defeat_number=defaultdict(int)
        for match in matches:
            gagnants.add(match[0])
            perdants.add(match[1])
            perdant=match[1]
            defeat_number[perdant]+=1
        liste_gagnants=sorted([player for player in list(gagnants) if player not in perdants])
        liste_perdants=sorted([key for key,val in defeat_number.items() if val==1])
        return [liste_gagnants,liste_perdants]
    


class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        arr=[0]*len(nums)
        even=sorted([nums[i] for i in range(0,len(nums)) if i%2==0])
        odd=sorted([nums[i] for i in range(0,len(nums)) if i%2!=0],reverse=True)
        for i in range(len(nums)):
            if i%2==0:
                arr[i]=even[i//2]
            else:
                arr[i]=odd[i//2]
        return arr
    


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if sorted(nums)==nums:
            return True
        if sorted(nums,reverse=True)==nums:
            return True
        return False
    

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        frequency=defaultdict(int)
        n=len(arr)
        for num in arr:
            frequency[num]+=1/n
        for key,val in frequency.items():
            if val>0.25:
                return key
            





    






 


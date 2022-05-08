class Solution:
    def isvalid(self, ip):
        if not ip.isnumeric():
            return False
        if len(ip) > 1 and ip[0] == '0':
            return False
        x = int(ip)
        if x > 255:
            return False
        return True

    def solve(self, ip, dots, path, ans, index):
        if dots >= 4:
            if dots == 4 and index == len(ip):
                #print(path)
                ans.append(path[:-1])
            return
        for i in range(index, min(index+3, len(ip))):
            if self.isvalid(ip[index:i+1]):
                #print(path)
                self.solve(ip, dots+1, path + ip[index:i+1] + '.', ans, i+1)

    def restoreIpAddresses(self, s: str):
        if len(s) > 12:
            return []
        path, ans = '', []
        self.solve(s, 0, path, ans, 0)
        print(ans)


if __name__ == '__main__':
    ip = '25525511135'
    Solution().restoreIpAddresses(ip)

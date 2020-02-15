import main as mn

def scrapeFollowers(name, ofname):
    Followers = tw.getProfileFollowerList(name, 2)
    folFile = open('followerAts.txt', 'w+')
    for x in Followers:
        folFile.write(x)
        if not x == Followers[len(Followers) - 1]:
            folFile.write('\n')
    folFile.close()

def profilesInfoSave(ifname = 'profiles.txt', ofname = 'profilesInfo.txt'):
    profiles = open(ifname, 'r')
    ats = profiles.read().split('\n')

    profilesInfoFile = open(ofname, 'w+')
    for x in ats:
        info = tw.getProfileInfo(x[1:])
        profilesInfoFile.write(x[1:] + ' ' + str(info[0]) + ' ' + str(info[1]))
        if not x == ats[len(ats) - 1]:
            profilesInfoFile.write('\n')
    profilesInfoFile.close()

def filterMilsav(ifname, ofname):
    ifile = open(ifname, 'r')
    ofile = open(ofname, 'w')

    pInfo = ifile.read().split('\n')
    for x in pInfo:
        y = str(x).split(' ')
        if abs(int(y[1]) - 86) < 2 and abs(int(y[2]) - 3) < 2:
            ofile.write(x + '\n')

    ifile.close()
    ofile.close()

tw = mn.TwitterBot()
tw.loginTwitter(1)

# scrapeFollowers('vaki_smithy', 'followerAts.txt')
# profilesInfoSave('followerAts.txt', 'profilesInfo.txt')
# filterMilsav('profilesInfo.txt', 'potMilsav.txt')



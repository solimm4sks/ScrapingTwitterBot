import main as mn

# used to get a list of users that follower a certain profile
def scrapeFollowers(name, ofname):
    Followers = list(tw.getProfileFollowerList(name, 2))
    folFile = open(ofname, 'w+')
    for x in Followers:
        folFile.write(x)
        if not x == Followers[len(Followers) - 1]:
            folFile.write('\n')
    folFile.close()

# used to get and save number of following and followers for a list of profiles
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

# used to, for example find all users with a certain following, followers range
def filterMilsav(ifname, ofname):
    ifile = open(ifname, 'r')
    ofile = open(ofname, 'w')

    pInfo = ifile.read().split('\n')
    for x in pInfo:
        y = str(x).split(' ')
        if abs(int(y[1]) - 86) < 2 and abs(int(y[2]) - 3) < 2: # literals should be customized
            ofile.write(x + '\n')

    ifile.close()
    ofile.close()

tw = mn.TwitterBot()
# if you have multiple accounts in the data.py file, the variable passed here decides which one is used
tw.loginTwitter(0)

# scrapeFollowers('vaki_smithy', 'followerAts.txt')
# profilesInfoSave('followerAts.txt', 'profilesInfo.txt')
# filterMilsav('profilesInfo.txt', 'potMilsav.txt')



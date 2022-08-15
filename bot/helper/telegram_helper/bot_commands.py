from bot import CMD_INDEX


class _BotCommands:
    def __init__(self):
        self.StartCommand = f'start'
        self.MirrorCommand = (f'mirror{CMD_INDEX}', f'mir')
        self.UnzipMirrorCommand = (f'unzipmirror{CMD_INDEX}', f'unzmir')
        self.ZipMirrorCommand = (f'zipmirror{CMD_INDEX}', f'zmir')
        self.QbMirrorCommand = (f'qbmirror{CMD_INDEX}', f'qbmir')
        self.QbUnzipMirrorCommand = (f'qbunzipmirror{CMD_INDEX}', f'qbunz}')
        self.QbZipMirrorCommand = (f'qbzipmirror{CMD_INDEX}', f'qbzmir')
        self.YtdlCommand = (f'ytd', f'yt')
        self.YtdlZipCommand = (f'ytdlz', f'ytz')
        self.LeechCommand = (f'leech{CMD_INDEX}', f'lc')
        self.UnzipLeechCommand = (f'unzipleech{CMD_INDEX}', f'unzlc')
        self.ZipLeechCommand = (f'zipleech{CMD_INDEX}', f'zlc')
        self.QbLeechCommand = (f'qbleech{CMD_INDEX}', f'qblc')
        self.QbUnzipLeechCommand = (f'qbunzipleech{CMD_INDEX}', f'qbuzlc')
        self.QbZipLeechCommand = (f'qbzipleech{CMD_INDEX}', f'qbzlc')
        self.YtdlLeechCommand = (f'ytdlleech{CMD_INDEX}', f'ytlc')
        self.YtdlZipLeechCommand = (f'ytdlzipleech{CMD_INDEX}', f'ytzlc')
        self.CloneCommand = f'cl'
        self.CountCommand = f'count{CMD_INDEX}'
        self.DeleteCommand = f'del'
        self.CancelMirror = f'cn'
        self.CancelAllCommand = f'cn_all'
        self.ListCommand = f'list'
        self.SearchCommand = f'search'
        self.StatusCommand = f'status'
        self.AuthorizedUsersCommand = f'users'
        self.AuthorizeCommand = f'authorize'
        self.UnAuthorizeCommand = f'unauthorize'
        self.AddSudoCommand = f'addsudo'
        self.RmSudoCommand = f'rmsudo'
        self.PingCommand = f'ping'
        self.RestartCommand = f'restart'
        self.StatsCommand = f'stats'
        self.HelpCommand = f'help'
        self.LogCommand = f'log'
        self.ShellCommand = f'shell{CMD_INDEX}'
        self.EvalCommand = f'eval{CMD_INDEX}'
        self.ExecCommand = f'exec{CMD_INDEX}'
        self.ClearLocalsCommand = f'clearlocals'
        self.LeechSetCommand = f'leechset'
        self.SetThumbCommand = f'setthumb'
        self.BtSelectCommand = f'btsel{CMD_INDEX}'
        self.RssListCommand = (f'rsslist{CMD_INDEX}', f'rl{CMD_INDEX}')
        self.RssGetCommand = (f'rssget{CMD_INDEX}', f'rg{CMD_INDEX}')
        self.RssSubCommand = (f'rsssub{CMD_INDEX}', f'rs{CMD_INDEX}')
        self.RssUnSubCommand = (f'rssunsub{CMD_INDEX}', f'rus{CMD_INDEX}')
        self.RssSettingsCommand = (f'rssset{CMD_INDEX}', f'rst{CMD_INDEX}')
        self.SleepCommand = f'sleep'

BotCommands = _BotCommands()

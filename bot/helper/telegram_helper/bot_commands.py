from bot import CMD_INDEX


class _BotCommands:
    def __init__(self):
        self.StartCommand = f'start'
        self.MirrorCommand = (f'mir', f'm')
        self.UnzipMirrorCommand = (f'unzmir', f'uzm')
        self.ZipMirrorCommand = (f'zmir', f'zm')
        self.QbMirrorCommand = (f'qbmir', f'qm')
        self.QbUnzipMirrorCommand = (f'qbunz', f'quzm')
        self.QbZipMirrorCommand = (f'qbzmir', f'qzm')
        self.YtdlCommand = (f'yt', f'y')
        self.YtdlZipCommand = (f'ytz', f'yz')
        self.LeechCommand = (f'lc', f'l')
        self.UnzipLeechCommand = (f'unzlc', f'uzl')
        self.ZipLeechCommand = (f'zlc', f'zl')
        self.QbLeechCommand = (f'qblc', f'ql')
        self.QbUnzipLeechCommand = (f'qbunzlc', f'quzl')
        self.QbZipLeechCommand = (f'qbzlc', f'qzl')
        self.YtdlLeechCommand = (f'ytlc', f'yl')
        self.YtdlZipLeechCommand = (f'ytzlc', f'yzl')
        self.CloneCommand = f'cl'
        self.CountCommand = f'count'
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
        self.ShellCommand = f'shell'
        self.EvalCommand = f'eval'
        self.ExecCommand = f'exec'
        self.ClearLocalsCommand = f'clearlocals'
        self.LeechSetCommand = f'leechset'
        self.SetThumbCommand = f'setthumb'
        self.BtSelectCommand = f'btsel'
        self.RssListCommand = (f'rsslist', f'rl')
        self.RssGetCommand = (f'rssget', f'rg')
        self.RssSubCommand = (f'rsssub', f'rs')
        self.RssUnSubCommand = (f'rssunsub', f'rus')
        self.RssSettingsCommand = (f'rssset', f'rst')
        self.SleepCommand = f'sleep'

BotCommands = _BotCommands()

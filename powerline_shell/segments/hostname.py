from ..utils import BasicSegment


class Segment(BasicSegment):
    def add_to_powerline(self):
        powerline = self.powerline
        if powerline.args.colorize_hostname:
            from lib.color_compliment import stringToHashToColorAndOpposite
            from lib.colortrans import rgb2short
            from socket import gethostname
            hostname = gethostname()
            FG, BG = stringToHashToColorAndOpposite(hostname)
            FG, BG = (rgb2short(*color) for color in [FG, BG])
            host_prompt = ' %s ' % hostname.split('.')[0]

            powerline.append(host_prompt, FG, BG)
        else:
            if powerline.args.shell == 'bash':
                host_prompt = ' \\h '
            elif powerline.args.shell == 'zsh':
                host_prompt = ' %m '
            else:
                import socket
                host_prompt = ' %s ' % socket.gethostname().split('.')[0]

            powerline.append(host_prompt,
                             powerline.theme.HOSTNAME_FG,
                             powerline.theme.HOSTNAME_BG)

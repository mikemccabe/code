#!/usr/bin/env python

"""
Copyright(c)2010 Mike McCabe. Software license AGPL version 3.
"""

def main(argv):
    import optparse

    parser = optparse.OptionParser(usage='usage: %prog [options] arg1 arg2',
                                   version='%prog 0.1',
                                   description='description goes here.')
    parser.add_option('-f', '--foo',
                      action='store_true',
                      default=False,
                      dest='foo',
                      help='Do the foo thing')
    parser.add_option('-i', '--intr',
                      action='store',
                      default=14,
                      dest='introo',
                      metavar='scoobage', # this shows up in help text
                      type='int',
                      help='test how int args work ... defaults to %default')
    opts, args = parser.parse_args(argv)
    print opts, args

    if opts.a and opts.b:
        parser.error("options -a and -b are mutually exclusive")

    parser.destroy()

    dostuff(opts, args)

def dostuff(opts, args):
    pass


if __name__ == '__main__':
    main(sys.argv[1:])

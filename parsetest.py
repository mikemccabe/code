import sys
import optparse




def main(argv):
    parser = optparse.OptionParser(usage='usage: %prog [options] arg1 arg2',
                                   version='%prog 0.1',
                                   description='a simple test script for trying out wtf to do with optparse... not sure why it seemed too daunting initially!')
    parser.add_option('-f', '--foo',
                      action='store_true',
                      default=False,
                      dest='foo',
                      help='Do the foo thing')
    def flag_callback(option, opt_str, value, parser):
        print 'flag_callback:'
        print '\toption:', repr(option)
        print '\topt_str:', opt_str
        print '\tvalue:', value
        print '\tparser:', parser
        return
    parser.add_option('--flag',
                      action="callback",
                      callback=flag_callback)
    def with_callback(option, opt_str, value, parser):
        print 'with_callback:'
        print '\toption:', repr(option)
        print '\topt_str:', opt_str
        print '\tvalue:', value
        print '\tparser:', parser
        return
    parser.add_option('--with', 
                      action="callback",
                      callback=with_callback,
                      type="string",
                      help="Include optional feature")
    parser.add_option('-i', '--intr',
                      action='store',
                      default=14,
                      dest='introo',
                      metavar='scoobage', # this shows up in help text
                      type='int',
                      help='test how int args work ... defaults to %default')
    parser.add_option('--addnum',
                      action='append',
                      dest='nums',
                      type='int',
                      help='test how append works')
    parser.add_option("-v", action="store_true", dest="verbose", default=True, help='be verbose')
    parser.add_option("-q", action="store_false", dest="verbose", help='be quiet')

    group = optparse.OptionGroup(parser, "Dangerous Options",
                        "Caution: use these options at your own risk.  "
                        "It is believed that some of them bite.")
    group.add_option("-g", action="store_true", help="Group option.")
    group.add_option("--ocrtype", action="store", choices=['this', 'that'], help='help str')
    group.add_option("--hidden", action="store_true", help=optparse.SUPPRESS_HELP)
    parser.add_option_group(group)
    group = optparse.OptionGroup(parser, "Boring options")
    group.add_option("--boring", action="store_true", help="so it is Default is %default")
    parser.add_option_group(group)
    parser.add_option('-a', action='store_true', help='not a and b')
    parser.add_option('-b', action='store_true', help='not a and b')


    group = optparse.OptionGroup(parser, 'Legend',
                                 'Here lies a complicated description string, with multiple lines\n'
                                 '    -like so\n'
                                 '    -and such\n'
                                 '    -also.')
    parser.add_option_group(group)

    opts, args = parser.parse_args(argv)
    print opts, args

    if opts.a and opts.b:
        parser.error("options -a and -b are mutually exclusive")

    parser.destroy()

if __name__ == '__main__':
    main(sys.argv[1:])

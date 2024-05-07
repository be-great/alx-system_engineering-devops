#!/usr/bin/env ruby
Sender = ARGV[0].scan(/from:(.*?)\]/)
Receive = ARGV[0].scan(/to:(.*?)\]/)
Flag = ARGV[0].scan(/flags:(.*?)\]/)
puts [Sender, Receive, Flag].join(',')
=begin
This program is a recreation of the "Evolution of Text" app that used to be on usingpython.com
This is also my first ruby program, I figured it is good to dive right in
=end

alphabet = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:\"ZXCVBNM<>? "
speed = 0.02

print "Enter text to evolve: "
target = gets.chomp

for char in target.split("")
    if !(alphabet.include? char)
        puts "Text contains invalid character #{char}"
        return
    end
end

word = ""
count = 0
while word != target
    for i in 0..target.length-1
        if word[i] != target[i]
            word[i] = alphabet[rand(alphabet.length)]
        end
    end
    puts word
    sleep speed
    count += 1
end

puts "\nFinal result obtained after #{count} iterations."
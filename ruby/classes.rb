class Bicycle
    @@total = 0

    def initialize(brand, color, gears)
        @@total += 1

        @serial = @@total
        @brand = brand
        @color = color
        @gears = gears

    end

    def get()
        return "This is a #{@brand} bicycle that is #{@color} and has #{@gears} gears. SN: #{@serial}"

    end
end

bike1 = Bicycle.new("Diamond", "black", 7)
bike2 = Bicycle.new("Krazy", "blue", 3)
bike3 = Bicycle.new("Speedster", "black", 2)
bike4 = Bicycle.new("Diamond", "gold", 15)

puts bike1.get()
puts bike2.get()
puts bike3.get()
puts bike4.get()
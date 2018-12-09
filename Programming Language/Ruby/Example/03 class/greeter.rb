class Greeter
  def initialize(name = "World")
    @name = name.capitalize
  end

  def say_hi
    puts "Hi, #{@name}!"
  end

  def say_bye
    puts "Bye, #{@name}, see you later~~"
  end
end

temp = Greeter.new("jaehun")

temp.say_hi()
temp.say_bye()

puts Greeter.instance_methods(false )
puts temp.respond_to?("name")
puts temp.respond_to?("say_hi")
puts temp.respond_to?("to_s")
class MegaGreeter
  attr_accessor :names

  def initialize(names = "World")
    @names = names
  end

  def say_hi
    if @names.nil?
      puts "..."
    elsif @names.respond_to?("each")
      @names.each do |name|
        puts "Hello, #{name}!"
      end
    else
      puts "Hello, #{names}!"
    end
  end

  def say_bye
    if @names.nil?
      puts "..."
    elsif @names.respond_to?("join")
      puts "Goodbye #{@names.join(", ")}. See you later~~~"
    else
      puts "Goodbye #{@names}. See you later~~~"
    end
  end
end

if __FILE__ == $0
  mg = MegaGreeter.new
  mg.say_hi
  mg.say_bye

  mg.names = "Jaehun"
  mg.say_hi
  mg.say_bye

  mg.names = ["Jaehun", "Chaehun", "Daehun", "Jaehan", "Jaehul"]
  mg.say_hi
  mg.say_bye

  mg.names = nil
  mg.say_hi
  mg.say_bye
end
# @param {Integer[]} citations
# @return {Integer}
def h_index(citations)
    result = 0
    (1..citations.size).each do |i|
        size = citations.select{|num| num >= i}.size
        if size >= i
            result = i
        end
    end
    result
end

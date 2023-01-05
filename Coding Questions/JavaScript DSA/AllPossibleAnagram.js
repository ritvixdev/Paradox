// print all possible anangram of given words

var arr = ['cat', 'dog', 'tac', 'god', 'act'];

var allAnagrams = function(arr) {
    var anagrams = {};
    arr.forEach(function(str) {
        var recurse = function(ana, str) {
            if (str === '') 
                anagrams[ana] = 1;
            for (var i = 0; i < str.length; i++)
                recurse(ana + str[i], str.slice(0, i) + str.slice(i + 1));
        };
        recurse('', str);
    });
    return Object.keys(anagrams);
}

console.log(allAnagrams(arr));
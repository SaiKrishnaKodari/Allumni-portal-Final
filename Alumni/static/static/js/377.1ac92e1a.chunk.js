(this.webpackJsonpalumini_portal_front_end=this.webpackJsonpalumini_portal_front_end||[]).push([[377],{493:function(s,n){!function(s){var n=["([\"'])(?:\\\\[^]|\\$\\([^)]+\\)|`[^`]+`|(?!\\1)[^\\\\])*\\1","<<-?\\s*([\"']?)(\\w+)\\2\\s[^]*?[\r\n]\\3"].join("|");s.languages["shell-session"]={info:{pattern:/^[^\r\n$#*!]+(?=[$#])/m,alias:"punctuation",inside:{path:{pattern:/(:)[\s\S]+/,lookbehind:!0},user:/^[^\s@:$#*!/\\]+@[^\s@:$#*!/\\]+(?=:|$)/,punctuation:/:/}},command:{pattern:RegExp("[$#](?:[^\\\\\r\n'\"<]|\\\\.|<<str>>)+".replace(/<<str>>/g,(function(){return n}))),greedy:!0,inside:{bash:{pattern:/(^[$#]\s*)[\s\S]+/,lookbehind:!0,alias:"language-bash",inside:s.languages.bash},"shell-symbol":{pattern:/^[$#]/,alias:"important"}}},output:/.(?:.*(?:[\r\n]|.$))*/},s.languages["sh-session"]=s.languages.shellsession=s.languages["shell-session"]}(Prism)}}]);
//# sourceMappingURL=377.1ac92e1a.chunk.js.map
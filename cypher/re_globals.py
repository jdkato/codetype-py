EXTRACT_RE = r"""
    [@|#]?[\w]+\(?|
    \+\+| # Scala
    :::| # Scala
    ::~| # C++
    ::| # C++, Haskell, Ruby, R, PHP
    =>| # C#, Rust, PHP
    <<(?!-)| # C++
    >>| # C++
    :\n| # Python
    <-| # Haskell, R
    ->| # Haskell, Rust, PHP, OCaml
    !!| # Haskell
    <<-| # R
    {-| # Haskell
    :=| # Go, OCaml
    <%| # Ruby
    %w| # Ruby
    ===| # PHP
    !==| # PHP
    \s\.\s| # PHP, Perl
    &&| # PHP
    =~| # Perl
    ~=| # Lua
    !\(| # Rust
    \[\]| # Java
    \.\.\.| # R
    \.\.| # Haskell
    \(\)| # Haskell, OCaml
    \$_| # PHP
    \#\[| # Rust
    1;| # Perl
    ;;| # OCaml
    \?\?\?| # Scala
    [~.@!?;:&\{\}\[\]\\#\/\|%\$`\*\)\(-,+]
"""
BLOCK_IGNORES = {
    "/*": [r"^\/\*.*$", r"^.*\*\/$", 3],
    "/+": [r"^\/\+.*$", r"^.*\+\/$", 3],
    "(*": [r"\(\*.*$", r"^.*\*\)$", 3],
    "'''": [r"^[\']{3}.*$", r"^.*[\']{3}$", 2],
    '"""': [r"^[\"]{3}.*$", r"^.*[\"]{3}$", 2],
    "{-": [r"^{-.*$", r"^.*-}$", 3],
    "=": [r"^=[^#>]*$", r"^=.*$", 3],
    "--[[": [r"^-{2,}\[{1,3}(.*)?$", r"^-{2,}\]{1,3}(.*)?$", 3],
    'r#"': [r'.*r#".*', r'\s*"#.*', 2]
}
INLINE_STRING = r"(?<!'|\"|`)('|\"|`)[^'\"`]*\1(?!'|\"|`)"
INLINE_IGNORES = {
    "#": [r"(?<!{-)(?<!r)#(?!-}).{1,}", 1],
    "//": [r"\/\/.*", 1],
    "--": [r"(?<!\w)--.*", 1],
    "/*": [r"/\*.*\*/", 1],
    "/+": [r"/\+.*\+/", 1],
    "(*": [r"\(\*.*\*\)", 1],
    "{-": [r"{-.*-}", 1],
    "'''": [r"^'{3}.*'{3}$", 2],
    '"""': [r'^"{3}.*"{3}$', 2]
}
INLINE_EXCEPTIONS = {
    "#": [
        r"#(include|!|define|undef|if|else|endif|import|pragma|\[|stdout)",
        # Lua `#` operator
        r"(?<!r)#([^\s-]{1,}$|.{1,}do\n?$|[^\s]*,.*\)|[^\s]{1,}\s==)",
        r"\(#.*\)",
        # OCaml
        r"\w#\w"
    ],
    "--": [
        # Perl `... --;`
        r".*\s--((@|\$|%).*)?;"
    ],
    "//": [
        # OCaml
        r"\(//\)"
    ]
}
FILE_TERMINATORS = [
    r"^1;$"
]

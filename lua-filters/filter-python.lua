-- Pandoc filter to process code blocks with class "py" 
-- containing Python code
-- the following chunk attributes are supported
--    - echo - should the source code been, showm default=true
--    - eval - should the Python code be evaluated, default=false
--    - cache - should the variables and the code beeing available in subsequent code chunks, default=false 

-- global variables
traverse = 'topdown'
local pycount = 1
local cache = false
local eval = false
local echo = true
local code = ""
local function toboolean(str)
    local bool = false
    if str == "true" then
        bool = true
    end
    return bool
end

function Meta (meta)
    cache = meta.py.cache or false
    eval  = meta.py.eval  or false
    echo  = meta.py.echo  or true
    return meta
end

-- TODO:
function Code(elem)
    x, y = string.find(elem.text,"py ")
    local result = elem.text
    if (y == 3) then
        local command = "python3 -c '" .. string.sub(elem.text,4,-1) .. ";'"
        local handle = io.popen(command)
        result = handle:read("*a")
        handle:close()
    end
    return pandoc.RawInline('HTML',result)
end

function CodeBlock(block)
    if block.classes[1] == "py" then
        local echo = block.attributes.echo or echo or true
        local eval = block.attributes.eval or eval or false
        local cache = block.attributes.cache or cache or false
        local result = ""
        if (tostring(cache) == "false") then
            code =""
        end
        if (eval) then
            w = io.open("chunk" .. pycount .. ".py","w")
            w:write("import os, sys\nsys.stdout = open(os.devnull, 'w')\n")
            w:write(code .. "\n")
            w:write("sys.stdout = sys.__stdout__\n")
            w:write(block.text)
            w:close()
            local command ="python3 chunk".. pycount ..".py"
            local handle = io.popen(command)
            result = handle:read("*a")
            handle:close()
            code = code .. block.text .. "\n"
            pycount = pycount + 1            

        end
        -- local fenced = '```\n%s\n```\n'
        if (echo) then
            if (result ~= "") then
                return {block,pandoc.CodeBlock(result)}
            else
                return {block}
            end
        else
            if (result ~= "") then
                --
                return { pandoc.CodeBlock(result) }
            else
                return {}
            end
        end
    end
end


-- Execute Meta first.
return {
    {Meta = Meta},
    {Code = Code},
    {CodeBlock = CodeBlock},
}

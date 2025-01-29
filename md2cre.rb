#!/usr/bin/env ruby
# Invoke with `ruby md2cre.rb filename.md`
# 
# Setup: `gem install redcarpet`

require 'rubygems'
require 'redcarpet'

class Creole < Redcarpet::Render::Base
  def normal_text(text)
    text
  end

  def link(link, title, content)
    "[[#{link}|#{content}]]"
  end

  def block_code(code, language)
    "\n{{{\n#{normal_text(code)}\n}}}\n"
  end

  def codespan(code)
    block_code(code, nil)
  end

  def header(title, level)
    case level
    when 1
      "\n= #{title} =\n"

    when 2
      "\n== #{title} ==\n"

    when 3
      "\n=== #{title} ===\n"
    end
  end

  def double_emphasis(text)
    "**#{text}**"
  end

  def emphasis(text)
    "//#{text}//"
  end

  def linebreak
    "\n"
  end

  def paragraph(text)
    "\n#{text}\n"
  end

  def list(content, list_type)
    case list_type
    when :ordered
      "\n#{content}\n"
    when :unordered
      "\n#{content}\n"
    end
  end

  def list_item(content, list_type)
    case list_type
    when :ordered
      "##{content.strip}\n"
    when :unordered
      "*#{content.strip}\n"
    end
  end
end

markdown = Redcarpet::Markdown.new(Creole, :fenced_code_blocks => true)

puts markdown.render(File.read(ARGV[0]))
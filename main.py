import nextcord
from nextcord.ext import commands
from nextcord import File, ButtonStyle
from nextcord.ui import Button, View


bot = commands.Bot(command_prefix="!", intents=nextcord.Intents.all())
                #  command_prefix 란 시작할 명령어


#"봇"이 준비 완료되면 터미널에 출력
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.slash_command(name="임베드", description="임베드를 만듬!")  # 명령
async def embed(ctx):
    embed = nextcord.Embed(
        title='제목',           # 제목과 설명은 임베드에 1개만 추가가 가능합니다
        description='설명',
        color=nextcord.Color(0xD3851F)  # 색상 코드
    )
    embed.add_field(name='필드 제목', value='필드 값', inline=False) # 필드

    embed.set_footer(text='푸터') # 임베드 1개에 1개만 작성 가능
    
    await ctx.send(embed=embed)

@bot.command(name="버튼")  # 명령 코드
async def buttons(ctx):


    link = Button(label="링크", url="https://forms.gle/zjQkW9MiNNdYe4kd6")  # 링크 버튼

    myview = View(timeout=180)
    myview.add_item(link)  # 링크 버튼

    await ctx.send("**클릭하여 설문지를 작성하시고 인증을 완료하세요**", view = myview)     #   버튼들 있는 메시지

    # 버튼의 색상을 정할 수가 있습니다 style=ButtonStyle 쪽에 있는 코드를 바꿔서 색을 변경할 수 있습니다
    # 링크를 담는 버튼은 제외됩니다
    #
    #파란 버튼 = blurple
    #빨간 버튼 = danger
    #회색 버튼 = gray
    #초록 버튼 = green

관리자_아이디 = '1239689583084703847'   # 관리자 아이디 넣기

@bot.slash_command(name="추방", description="유저를 추방함")
async def kick(ctx: nextcord.Interaction, 
               멤버: nextcord.Member = nextcord.SlashOption(description="추방할 멤버를 골라주세요.", required=True),
               사유: str = nextcord.SlashOption(description="사유를 적어주세요", required=False)):
    if str(ctx.user.id) == 관리자_아이디:   # 관리자_아이디에 적힌 유저만 사용 가능
    
        if ctx.user.guild_permissions.kick_members:
            await 멤버.kick(reason=사유) # 추방코드
            await ctx.response.send_message(f'{멤버} 님이 추방되었습니다\n**사유** : {사유}')
        else:
            # 봇이 멤버를 추방할 권한이 없을 떄
            await ctx.response.send_message("구성원을 추방할 권한이 없습니다.", ephemeral=True)
    else:
        # 관리자가 아닌 사람이 이 명령어를 입력하였을 때
        await ctx.response.send_message("이 명령어를 사용할 권한이 없습니다.", ephemeral=True) 



        


@bot.slash_command(name="차단", description="유저를 차단함")
async def ban(ctx: nextcord.Interaction, 
              멤버: nextcord.Member = nextcord.SlashOption(description="차단할 멤버를 골라주세요.", required=True),
              사유: str = nextcord.SlashOption(description="사유를 적어주세요", required=False)):
    if str(ctx.user.id) == 관리자_아이디:  # 관리자_아이디에 적힌 유저만 사용 가능
        if ctx.user.guild_permissions.ban_members:
            await 멤버.ban(reason=사유)  # 차단코드
            await ctx.response.send_message(f'{멤버} 님이 차단되었습니다\n**사유** : {사유}')
        else:
            # 봇이 멤버를 차단할 권한이 없을 떄
            await ctx.response.send_message("구성원을 차단할 수 있는 권한이 없습니다.", ephemeral=True)
    else:
        # 관리자가 아닌 사람이 이 명령어를 입력하였을 때
        await ctx.response.send_message("이 명령어를 사용할 권한이 없습니다.", ephemeral=True)




              


bot.run("token") #토큰
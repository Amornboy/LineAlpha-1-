# -*- coding: utf-8 -*-
from LineAlpha import LineClient
from LineAlpha.LineApi import LineTracer
from LineAlpha.LineThrift.ttypes import Message
from LineAlpha.LineThrift.TalkService import Client
import datetime, locale, random ,sys, re, string, urllib2, os
import json, urllib2
import time
import TLAlpha
from TLAlpha.Api import Channel
from TLAlpha.lib.Gen.ttypes import Message
from threading import Thread
import time
import sys
import ctypes
import datetime
import random
kongoutl = TLAlpha.LINE()
kongoutl.login("tdjyfxhj@gmail.com","tanuki1192","da01d4562c10dc70b1b9e27250382236c55357b3193af115838f1009022e2240")
kongou = LineClient()
kongou._login("opm78d141@yahoo.co.jp","tanuki","78d2cda1f0881bf4b4cc333eb7558f68e5aae31a2309424e825e2f2bb8250b72")
kongou._loginresult()
haruna = LineClient()
haruna._login("opm37564@gmail.com","tanuki1192","6e3ee39deb0d4a3c5db476b1557692d689efc5b7e7b4ba3a8eaebee250728587")
hiei = LineClient()
hiei._login("opm48d141@gmail.com","tanuki1192","de54ee970639c8f74272203a84785115e9174b31922ad3f7ecfc7a54df71a7a8")
kirisima = LineClient()
kirisima._login("asuna1192kirito@gmail.com","tanuki1192","0995bd42b46d86535f7996ad9fb52186c34272f433a34e2c8ae6971ecdf0518c")
kicker1 = LineClient()
kicker1._login("opm65d141@gmail.com","tanuki1192","4b944c7b094ad76d9daefb5b41a8564b80efdd862f84f7c8af3493432393299c")
kickerA = LineClient()
kickerA._login("opm01d141@gmail.com","tanuki1192","f43449671eda4412e0e0952e083b37e5801e48dd9a2f257ffce3c1130afa5ebc")
kickerB = LineClient()
kickerB._login("opm09d141@gmail.com","tanuki1192","3c656bffceaf3834ef2984768baad57120faa07c7b9d9a00cddb15986841881e")
kickerC = LineClient()
kickerC._login("rikumishio@gmail.com","tanuki1192","fd9028c5bd36f8f188dbe915fecf67812daa471d1860ea55987b52420376e20d")
kickerD = LineClient()
kickerD._login("opm77d141@gmail.com","tanuki1192","1e58a92f3910519f874b10735034f47042d2281118e7bc27a460e65d65c4f7b2")
kickerE = LineClient()
kickerE._login("opm11d141@yahoo.co.jp","tanuki","db5a014dda2b4321e5a864574c495729947dbe1860364a157608a48834ddf38a")
kickerF = LineClient()
kickerF._login("opm46d141@gmail.com","tanuki","0830d01d524f9211cccee697e5b08044f977ba1e3e131c83298a33e3fd76f61b")
kickerG = LineClient()
kickerG._login("opm77d141@yahoo.co.jp","tanuki","c55b9990b20847e7e8f82c9df82ea847d5fdc6ccc3f8d91a7ee300f32bb7346a")
kickerH = LineClient()
kickerH._login("opm02d141@gmail.com","tanuki","7293cb377ec1cc703f57f2e2a2757c0616cd2ed145e4c399ba1837d0e0dfb9a6")
kickerI = LineClient()
kickerI._login("yuukiasuna220@gmail.com","tanuki","8950d4f558d9d5d230dca0f83c53013728f7ae3aac2d85bcf252e470459522ae")
kickerJ = LineClient()
kickerJ._login("ryata765@ahk.jp","sora0326","0ca26eaa2a7db842fd7669cf178cf3014f594734ec7ea69c0435cb2072b2652f")
kickerK = LineClient()
kickerK._login("kirito0562@gmail.com","tanuki","1e8d158ae69dcf2f1d6fa45ee4ed75493daad1c7f5c36c295aa235b148906b30")
kickerL = LineClient()
kickerL._login("opm31141d@yahoo.co.jp","tanuki","1f8a9a4338dcebc1ea8d73d00493aa4083d0bdffdfa0067bf32b04f8be2caed6")
kickerL._loginresult()
K = [haruna,hiei,kirisima,kickerA,kickerB,kickerC,kickerD,kickerE,kickerF,kickerG,kickerH,kickerI,kickerJ,kickerK,kickerL]
tracer = LineTracer(kongou)
"""
kickerAs = kickerA.getProfile()
kickerBs = kickerB.getProfile()
kickerCs = kickerC.getProfile()
kickerDs = kickerD.getProfile()
kickerEs = kickerE.getProfile()
kickerFs = kickerF.getProfile()
kickerGs = kickerG.getProfile()
kickerHs = kickerH.getProfile()
kickerIs = kickerI.getProfile()
kickerJs = kickerJ.getProfile()
kickerKs = kickerK.getProfile()
kickerLs = kickerL.getProfile()
kickerAs.displayName = "kickerA"
kickerA.updateProfile(kickerAs)
kickerBs.displayName = "kickerB"
kickerB.updateProfile(kickerBs)
kickerCs.displayName = "kickerC"
kickerC.updateProfile(kickerCs)
kickerDs.displayName = "kickerD"
kickerD.updateProfile(kickerDs)
kickerEs.displayName = "kickerE"
kickerE.updateProfile(kickerEs)
kickerFs.displayName = "kickerF"
kickerF.updateProfile(kickerFs)
kickerGs.displayName = "kickerG"
kickerG.updateProfile(kickerGs)
kickerHs.displayName = "kickerH"
kickerH.updateProfile(kickerHs)
kickerIs.displayName = "kickerI"
kickerI.updateProfile(kickerIs)
kickerJs.displayName = "kickerJ"
kickerJ.updateProfile(kickerJs)
kickerKs.displayName = "kickerK"
kickerK.updateProfile(kickerKs)
kickerLs.displayName = "kickerL"
kickerL.updateProfile(kickerLs)
"""
d = datetime.datetime.today()
msg = Message()
gids = msg.to
sakujyo = []
wait = {
    'calc':{},
    'readPoint':{},
    'readMember':{},
    'musi':{},
    'kickout':{},
    'howaito':{},
    'kicks':{},
    'sTime':"",
    'bye':{},
    'waittime':{},
    'sTimeCount':"",
    'MessageCount':{},
    }
res = {
    'num':{},
    'us':{},
    'au':{},
    }
admins = ["u761056961757de99d6d1f5dd4cacae0e",""]
kongous = [kongou.getProfile().mid]
bots = [haruna.getProfile().mid, hiei.getProfile().mid, kirisima.getProfile().mid, kickerA.getProfile().mid, kickerB.getProfile().mid, kickerC.getProfile().mid, kickerD.getProfile().mid, kickerE.getProfile().mid, kickerF.getProfile().mid, kickerG.getProfile().mid, kickerH.getProfile().mid, kickerI.getProfile().mid, kickerJ.getProfile().mid, kickerK.getProfile().mid, kickerL.getProfile().mid]
profile = kongou.getProfile()
protecturl = {}
protecton = {}
of = {}
keru = {}
bls = {}
howai = {}
targetA = {}
targetB = {}
targetC = {}
targetA1 = []
delete = {}
sex = []
def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text

    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    kongou._client.sendMessage(0, mes)
def sendContact(to,mid):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = None
    mes.contentType = 13
    mes.contentMetadata = {'mid':mid}
    kongou._client.sendMessage(0, mes)

def sendMessageK(to,text,contentMetadata={},contentType=0):
    mes = Message()
    mes.to,mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    hiei._client.sendMessage(0, mes)

def sendContactK(to, mid):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = None
    mes.contentType = 13
    mes.contentMetadata = {'mid':mid}
    hiei._client.sendMessage(0, mes)
def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["/",">",";","^","%","$","＾","?","/"]
    for texX in tex:
        for command in commands:
            if string ==texX + command:
                return True
    return False

def cmi(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["/",">",";","^","%","$","＾","?","/"]
    for texX in tex:
        for command in commands:
            if texX + command in string:
                return True
    return False

def cmd(text, commands):
    for command in commands:
        if command in text:
            return True
    return False
def NOTIFIED_INVITE_INTO_GROUP(op):
    msg = op.message
    s = open("whitelist.txt","r")
    s1 = s.read()
    s.close()
    try:
        if op.param1 in protecton:
            Inviter = op.param3.replace("",',')
            InviterX = Inviter.split(",")
            mid = op.param2
            contact = kongou.getContact(mid)
            kongou.cancelGroupInvitation(op.param1, InviterX)
            sendMessage(op.param1, "提督〜！現在は招待できない設定になってるよ〜！")
            s = open("whitelist.txt","r")
            s1 = s.read()
            s.close()
            if op.param2 in s1:
                pass
            else:
                kirisima.kickoutFromGroup(op.param1, [mid])
        else:
            pass
    except Exception as e:
        print e
    try:
        with open("blacklist.txt", "r") as f:
            group = kongou.getGroup(op.param1)
            BL1 = [l.rstrip() for l in f]
            gInviMids = [contact.mid for contact in group.invitee]
            blacklist = []
            for tag in BL1:
                for src in gInviMids:
                    if tag == src:
                        blacklist.append(tag)
            try:
                hiei.cancelGroupInvitation(op.param1,blacklist)
                sendMessage(op.param1,"ブラックリストユーザーの招待を検知したのでキャンセルしました！")
            except:
                pass
    except Exception as e:
        print e
        pass
    try:
        if profile.mid in op.param3:
            if op.param2 in s1:
                kongou.acceptGroupInvitation(op.param1)
                group = kongou.getGroup(op.param1)
                if group.preventJoinByTicket == False:
                    Ticket = kongou.reissueGroupTicket(op.param1)
                    gid = op.param1
                    for bot in K:
                        bot.acceptGroupInvitationByTicket(gid,Ticket)
                    sendMessage(op.param1, "お")
                else:
                    group.preventJoinByTicket = False
                    kongou.updateGroup(group)
                    Ticket = kongou.reissueGroupTicket(op.param1)
                    gid = op.param1
                    for bot in K:
                        bot.acceptGroupInvitationByTicket(gid,Ticket)
                    sendMessage(op.param1, "お")
            elif op.param2 in admins:
                kongou.acceptGroupInvitation(op.param1)
                if group.preventJoinByTicket == False:
                    Ticket = kongou.reissueGroupTicket(op.param1)
                    gid = op.param1
                    for bot in K:
                        bot.acceptGroupInvitationByTicket(gid,Ticket)
                    sendMessage(op.param1, "お")
                else:
                    group.preventJoinByTicket = False
                    kongou.updateGroup(group)
                    Ticket = kongou.reissueGroupTicket(op.param1)
                    gid = op.param1
                    for bot in K:
                        bot.acceptGroupInvitationByTicket(gid,Ticket)
                    sendMessage(op.param1, "お")
            else:
                kongou.acceptGroupInvitation(op.param1)
                kongou.leaveGroup(op.param1)
    except Exception as e:
        pass
tracer.addOpInterrupt(13, NOTIFIED_INVITE_INTO_GROUP)
def NOTIFIED_KICKOUT_FROM_GROUP(op):
    group = kongou.getGroup(op.param1)
    group1 = hiei.getGroup(op.param1)
    s = open("whitelist.txt","r")
    s1 = s.read()
    s.close()
    BL = open("blacklist.txt","r")
    blacklist = BL.read()
    BL.close()
    mid = op.param2
    try:
        if op.param3 in kongous:
            if group1.preventJoinByTicket == False:
                url = hiei.reissueGroupTicket(op.param1)
                gid = op.param1
                kongou.acceptGroupInvitationByTicket(gid,url)
                if mid in blacklist:
                    kickerB.kickoutFromGroup(gid, [mid])
                elif mid in s1:
                    pass
                else:
                    e = open("blacklist.txt","a")
                    e.write(mid + "\n")
                    e.close()
                    kickerB.kickoutFromGroup(gid, [mid])
            else:
                group1.preventJoinByTicket = False
                hiei.updateGroup(group1)
                url = hiei.reissueGroupTicket(op.param1)
                gid = op.param1
                kongou.acceptGroupInvitationByTicket(gid,url)
                if mid in blacklist:
                    kickerB.kickoutFromGroup(gid, [mid])
                elif mid in s1:
                    pass
                else:
                    e = open("blacklist.txt","a")
                    e.write(mid + "\n")
                    e.close()
                    kickerB.kickoutFromGroup(gid, [mid])
        elif op.param3 in K:
            if group.preventJoinByTicket == False:
                url = kongou.reissueGroupTicket(op.param1)
                gid = op.param1
                for bot in K:
                    bot.acceptGroupInvitationByTicket(gid,url)
                if mid in blacklist:
                    kickerB.kickoutFromGroup(gid, [mid])
                elif mid in s1:
                    pass
                else:
                    e = open("blacklist.txt","a")
                    e.write(mid + "\n")
                    e.close()
                    kickerB.kickoutFromGroup(gid, [mid])
            else:
                group.preventJoinByTicket = False
                kongou.updateGroup(group)
                url = kongou.reissueGroupTicket(op.param1)
                gid = op.param1
                for bot in K:
                    bot.acceptGroupInvitationByTicket(gid,url)
                if mid in blacklist:
                    kickerB.kickoutFromGroup(gid, [mid])
                elif mid in s1:
                    pass
                else:
                    e = open("blacklist.txt","a")
                    e.write(mid + "\n")
                    e.close()
                    kickerB.kickoutFromGroup(gid, [mid])
        else:
            if group.preventJoinByTicket == False:
                url = kongou.reissueGroupTicket(op.param1)
                gid = op.param1
                for bot in K:
                    bot.acceptGroupInvitationByTicket(gid,url)
                if mid in blacklist:
                    kickerB.kickoutFromGroup(gid, [mid])
                elif mid in s1:
                    pass
                else:
                    e = open("blacklist.txt","a")
                    e.write(mid + "\n")
                    e.close()
                    kickerB.kickoutFromGroup(gid, [mid])
    except Exception as e:
        print e
tracer.addOpInterrupt(19, NOTIFIED_KICKOUT_FROM_GROUP)
def RECEIVE_MESSAGE(op):
    msg = op.message
    s = open("whitelist.txt","r")
    s1 = s.read()
    s.close()
    try:
        if 13 == msg.contentType:
            mid = msg.from_
            s = open("whitelist.txt","r")
            s1 = s.read()
            s.close()
            BL = open("blacklist.txt","r")
            blacklist = BL.read()
            BL.close()
            try:
                if 'mid' in msg.contentMetadata:
                    contact = kongou.getContact(msg.contentMetadata["mid"])
                    mid = msg.contentMetadata["mid"]
                    if msg.to in keru:
                        group = kongou.getGroup(msg.to)
                        if group.preventJoinByTicket == False:
                            url = kongou.reissueGroupTicket(msg.to)
                            gid = msg.to
                            kicker1.acceptGroupInvitationByTicket(gid, url)
                            try:
                                kicker1.kickoutFromGroup(gid, [mid])
                            except:
                                pass
                            kicker1.leaveGroup(gid)
                            group.preventJoinByTicket = True
                            kongou.updateGroup(group)
                        else:
                            group.preventJoinByTicket = False
                            kongou.updateGroup(group)
                            url = kongou.reissueGroupTicket(msg.to)
                            gid = msg.to
                            kicker1.acceptGroupInvitationByTicket(gid, url)
                            try:
                                kicker1.kickoutFromGroup(gid, [mid])
                            except:
                                pass
                            kicker1.leaveGroup(gid)
                            group.preventJoinByTicket = True
                            kongou.updateGroup(group)
                        try:
                            del keru[msg.to]
                        except Exception as e:
                            print e
                            pass
                    elif msg.to in bls:
                        if mid in blacklist:
                            sendMessage(msg.to,"このユーザーはすでにブラックリストに登録されているよ〜！")
                        elif mid in s1:
                            sendMessage(msg.to,"このユーザーはブラックリストに登録することができないよ〜！")
                        else:
                            e = open("blacklist.txt","a")
                            e.write(mid + "\n")
                            e.close()
                            sendMessage(msg.to,"ブラックリストに登録しました。\n終了する場合は「/ブラックリスト登録終了」と送信してください！")
                    elif msg.to in delete:
                        with open("blacklist.txt", "r") as f:
                            target = [l.rstrip() for l in f]
                            print mid
                            if mid in target:
                                for i in target:
                                    print i
                                    if i == mid:
                                        pass
                                    else:
                                        sakujyo.append(i + "\n")
                                f = open("blacklist.txt", "w")
                                f.close()
                                s = open("blacklist.txt", "a")
                                for i in sakujyo:
                                    s.write(i)
                                s.close()
                                sendMessage(msg.to,"削除したよ〜！")
                                del sakujyo[:]
                                try:
                                    del delete[msg.to]
                                except:
                                    pass
                            else:
                                sendMessage(msg.to,"このユーザーはブラックリストに登録されてないよ！")
                                try:
                                    del delete[msg.to]
                                except:
                                    pass
                    elif msg.to in howai:
                        if mid in s1:
                            sendMessage(msg.to,"提督〜！このユーザーはすでにホワイトリストユーザーだよ〜！")
                            try:
                                del howai[msg.to]
                            except:
                                pass
                        else:
                            k = open("whitelist.txt","a")
                            k.write(mid + "\n")
                            k.close()
                            sendMessage(msg.to,"ホワイトリストに登録したよ〜！")
                            try:
                                del howai[msg.to]
                            except:
                                pass
                    else:
                        if mid in blacklist:
                            sendMessage(msg.to, "[Name]\n" + msg.contentMetadata["displayName"] + "\n[Mid]\n" + msg.contentMetadata["mid"] + "\n[アイコン]\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[cover]\n" + kongoutl.channel.getCover(mid).encode('utf_8') + "\n[ブラックリスト]\n登録されています。")
                        else:
                            contact = kongou.getContact(msg.contentMetadata["mid"])
                            sendMessage(msg.to, "[Name]\n" + contact.displayName + "\n[Mid]\n" + msg.contentMetadata["mid"] + "\n[アイコン]\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[cover]\n" + kongoutl.channel.getCover(mid).encode('utf_8') + "\n[ブラックリスト]\n登録されていません。")
            except Exception as e:
                print e

        elif 16 == msg.contentType:
            BL = open("blacklist.txt","r")
            blacklist = BL.read()
            BL.close()
            if 'text' not in msg.contentMetadata:
                if 'mediaOid' in msg.contentMetadata:
                    Object = msg.contentMetadata['mediaOid'].replace("svc=myhome|sid=h|","")
                    if msg.contentMetadata['mediaType'] == 'V':
                        if msg.contentMetadata['serviceType'] == 'GB':
                            sendMessage(msg.to, kongou.getContact(msg.from_).displayName + "さんがノートに投稿しました。\n\n[postURL]\n" + msg.contentMetadata['postEndUrl'] + "\n[ObjectURL]\nhttps://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&oid=" + msg.contentMetadata['mediaOid'] + "\n[MediaURL]\nhttps://obs-us.line-apps.com/myhome/h/download.nhn?oid=" + msg.contentMetadata['mediaOid'])
                        else:
                            sendMessage(msg.to, kongou.getContact(msg.from_).displayName + "さんが" + msg.contentMetadata['serviceName'] + "さんの投稿を共有しました。\n\n[postURL]\n" + msg.contentMetadata['postEndUrl'] + "\n[ObjectURL]\nhttps://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&" + Object + "\n[MediaURL]\nhttps://obs-us.line-apps.com/myhome/h/download.nhn?" + Object)
                    elif msg.contentMetadata['mediaType'] == 'I':
                        if msg.contentMetadata['serviceType'] == 'AB':
                            sendMessage(msg.to, kongou.getContact(msg.from_).displayName + "さんがアルバムに投稿しました。\n\n""[アルバム名]\n" + msg.contentMetadata['albumName'] + "\n\n[アルバムURL]\n" + msg.contentMetadata['postEndUrl'])
                    else:
                        if msg.contentMetadata['serviceType'] == 'GB':
                            sendMessage(msg.to, kongou.getContact(msg.from_).displayName + "さんがノートに投稿しました。\n\n[postURL]\n" + msg.contentMetadata['postEndUrl'] + "\n[ObjectURL]\nhttps://obs-us.line-apps.com/myhome/h/download.nhn?oid=" + msg.contentMetadata['mediaOid'])
                        else:
                            sendMessage(msg.to, kongou.getContact(msg.from_).displayName + "さんが" + msg.contentMetadata['serviceName'] + "さんの投稿を共有しました。\n\n[postURL]\n" + msg.contentMetadata['postEndUrl'] + "\n[ObjectURL]\nhttps://obs-us.line-apps.com/myhome/h/download.nhn?" + Object)
                elif 'stickerId' in msg.contentMetadata:
                    if msg.contentMetadata['serviceType'] == 'GB':
                        sendMessage(msg.to, kongou.getContact(msg.from_).displayName + "さんがノートに投稿しました。\n\n[postURL]\n" + msg.contentMetadata['postEndUrl'] + "\n[Package]\nhttp://line.me/R/shop/detail/" + msg.contentMetadata['packageId'])
                    else:
                        sendMessage(msg.to, kongou.getContact(msg.from_).displayName + "さんが" + msg.contentMetadata['serviceName'] + "さんの投稿を共有しました。\n\n[postURL]\n" + msg.contentMetadata['postEndUrl'] + "\n[Package]\nhttp://line.me/R/shop/detail/" + msg.contentMetadata['packageId'])
                else:
                    if msg.contentMetadata['serviceType'] == 'GB':
                        sendMessage(msg.to, kongou.getContact(msg.from_).displayName + "さんがノートに投稿しました。\n\n[postURL]\n" + msg.contentMetadata['postEndUrl'])
                    else:
                        sendMessage(msg.to, kongou.getContact(msg.from_).displayName + "さんが" + msg.contentMetadata['serviceName'] + "さんの投稿を共有しました。\n\n[postURL]\n" + msg.contentMetadata['postEndUrl'])
                        print(kongou.getContact(msg.from_).displayName + "さんが" + msg.contentMetadata['serviceName'] + "さんの投稿を共有しました。\n\n[postURL]\n" + msg.contentMetadata['postEndUrl'])
            else:
                if 'mediaOid' in msg.contentMetadata:
                    Object = msg.contentMetadata['mediaOid'].replace("svc=myhome|sid=h|","")
                    if msg.contentMetadata['mediaType'] == 'V':
                       if msg.contentMetadata['serviceType'] == 'GB':
                            sendMessage(msg.to, kongou.getContact(msg.from_).displayName + "さんがノートに投稿しました。\n\n[postURL]\n" + msg.contentMetadata['postEndUrl'] + "\n[text]\n" + msg.contentMetadata['text'] + "\n[ObjectURL]\nhttps://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&oid=" + msg.contentMetadata['mediaOid'] + "\n[MediaURL]\nhttps://obs-us.line-apps.com/myhome/h/download.nhn?oid=" + msg.contentMetadata['mediaOid'])
                       else:
                            sendMessage(msg.to, kongou.getContact(msg.from_).displayName + "さんが" + msg.contentMetadata['serviceName'] + "さんの投稿を共有しました。\n\n[postURL]\n" + msg.contentMetadata['postEndUrl'] + "\n[text]\n" + msg.contentMetadata['text'] + "\n[ObjectURL]\nhttps://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&" + Object + "\n[MediaURL]\nhttps://obs-us.line-apps.com/myhome/h/download.nhn?" + Object)
                    else:
                        if msg.contentMetadata['serviceType'] == 'GB':
                            sendMessage(msg.to, kongou.getContact(msg.from_).displayName + "さんがノートに投稿しました。\n\n[postURL]\n" + msg.contentMetadata['postEndUrl']+ "\n[text]\n" + msg.contentMetadata['text'] + "\n[ObjectURL]\nhttps://obs-us.line-apps.com/myhome/h/download.nhn?oid=" + msg.contentMetadata['mediaOid'])
                        else:
                            sendMessage(msg.to, kongou.getContact(msg.from_).displayName + "さんが" + msg.contentMetadata['serviceName'] + "さんの投稿を共有しました。\n\n[postURL]\n" + msg.contentMetadata['postEndUrl']+ "\n[text]\n" + msg.contentMetadata['text'] + "\n[ObjectURL]\nhttps://obs-us.line-apps.com/myhome/h/download.nhn?" + Object)
                elif 'stickerId' in msg.contentMetadata:
                    if msg.contentMetadata['serviceType'] == 'GB':
                        sendMessage(msg.to, kongou.getContact(msg.from_).displayName + "さんがノートに投稿しました。\n\n[postURL]\n" + msg.contentMetadata['postEndUrl'] + "\n[text]\n" + msg.contentMetadata['text'] + "\n[Package]\nhttp://line.me/R/shop/detail/" + msg.contentMetadata['packageId'])
                    else:
                        sendMessage(msg.to, kongou.getContact(msg.from_).displayName + "さんが" + msg.contentMetadata['serviceName'] + "さんの投稿を共有しました。\n\n[postURL]\n" + msg.contentMetadata['postEndUrl'] + "\n[text]\n" + msg.contentMetadata['text'] + "\n[Package]\nhttp://line.me/R/shop/detail/" + msg.contentMetadata['packageId'])
                else:
                    if msg.contentMetadata['serviceType'] == 'GB':
                        sendMessage(msg.to, kongou.getContact(msg.from_).displayName + "さんがノートに投稿しました。\n\n[postURL]\n" + msg.contentMetadata['postEndUrl'] + "\n[text]\n" + msg.contentMetadata['text'])
                    else:
                        sendMessage(msg.to, kongou.getContact(msg.from_).displayName + "さんが" + msg.contentMetadata['serviceName'] + "さんの投稿を共有しました。\n\n[postURL]\n" + msg.contentMetadata['postEndUrl'] + "\n[text]\n" + msg.contentMetadata['text'])

        elif 0 == msg.contentType:
            n = open("blacklist.txt","r")
            n1 = n.read()
            n.close()
            try:
                kongou.leaveRoom(msg.to)
            except:
                pass
            if cms(msg.text, ["bye"]):
                if msg.from_ in s1:
                    kongou.leaveGroup(msg.to)
                    for v in K:
                        v.leaveGroup(msg.to)
                elif msg.from_ in admins:
                    kongou.leaveGroup(msg.to)
                    for v in K:
                        v.leaveGroup(msg.to)
                else:
                    pass
            elif msg.from_ in n1:
                if msg.to in of:
                    pass
                else:
                    hiei.kickoutFromGroup(msg.to,[msg.from_])
            elif cms(msg.text, ["protect name on","protect　name　on"]):
                gid = msg.to
                group = kongou.getGroup(gid)
                s = open(gid + '.txt',"w")
                s.write(group.name)
                s.close()
                sendMessage(msg.to, "提督〜！プロテクト機能を有効にしたよ！")
            elif cms(msg.text,["保護レベル1"]):
                if msg.from_ in s1:
                    sendMessage(msg.to,"提督〜！保護機能をレベル1にしたよ！")
                    of[msg.to] = "of"
                else:
                    sendMessage(msg.to,"提督には権限がないよ！")
            elif cms(msg.text,["保護レベル2"]):
                if msg.from_ in s1:
                    sendMessage(msg.to,"提督〜！保護機能をレベル2にしたよ！")
                    del of[msg.to]
                else:
                    sendMessage(msg.to,"提督には権限がないよ！")
            elif cms(msg.text, ["protect　name　off","protect name off"]):
                try:
                    if msg.from_ in admins:
                        gid = msg.to
                        os.remove(gid + ".txt")
                        sendMessage(msg.to, "提督〜！プロテクト機能を無効にしたよ！")
                    elif msg.from_ in s1:
                        gid = msg.to
                        os.remove(gid + ".txt")
                        sendMessage(msg.to, "提督〜！プロテクト機能を有効にしたよ！")
                except:
                    sendMessage(gid, "プロテクト機能はすでに有効だよ！！")
                    pass
            elif cms(msg.text, ["既読ポイント設定"]):
                sendMessage(msg.to, "既読ポイントを設定したよ！\n確認したい場合は「/既読確認」とコメントしてね！")
                try:
                    del wait['readPoint'][msg.to]
                    del wait['readMember'][msg.to]
                    del wait['waittime'][msg.to]
                except:
                    pass
                wait['readPoint'][msg.to] = msg.id
                wait['readMember'][msg.to] = ""
                wait['waittime'][msg.to] = datetime.datetime.today().strftime('%Y-%m-%d- %H:%M:%S')

            elif cms(msg.text, ["既読確認"]):
                if msg.to in wait['readPoint']:
                    sendMessage(msg.to, "既読を付けた人は" + wait['readMember'][msg.to] + "\nﾃﾞｰｽ！\n既読ポイント設定日時\n" + "[" + wait['waittime'][msg.to] + "]")
                else:
                    sendMessage(msg.to, "既読ポイントが設定されていないよ！\nでも！「/既読ポイント設定」ということで設定できるよ！")
            elif cms(msg.text,["ブラックリスト表示"]):
                if msg.from_ in admins:
                    with open("blacklist.txt", "r") as f:
                        target = [l.rstrip() for l in f]
                        for i in target:
                            print i
                            sendContact(msg.to,i)
                        sendMessage(msg.to,"以上がブラックリストユーザーだよ！")
            elif cms(msg.text, ["ブラックリスト削除"]):
                gid = msg.to
                if msg.from_ in s1:
                    sendMessage(msg.to, "連絡先を送信してね！")
                    delete[gid] = "delete"
                elif msg.from_ in admins:
                    sendMessage(msg.to, "連絡先を送信してね！")
                    delete[gid] = "delete"
            elif cms(msg.text, ["kick"]):
                gid = msg.to
                if msg.from_ in s1:
                    sendMessage(msg.to, "連絡先を送信してね！")
                    keru[gid] = "keru"
                elif msg.from_ in admins:
                    sendMessage(msg.to, "連絡先を送信してね！")
                    keru[gid] = "keru"
            elif cms(msg.text, ["ホワイトリスト登録"]):
                gid = msg.to
                if msg.from_ in admins:
                    sendMessage(msg.to, "ホワイトリストに登録するユーザーの連絡先を送信してね！")
                    howai[gid] = "howai"
            elif cms(msg.text, ["ブラックリスト登録"]):
                gid = msg.to
                if msg.from_ in admins:
                    sendMessage(msg.to, "ブラックリストに登録するユーザーの連絡先を送信してね！")
                    bls[gid] = "bls"
                elif msg.from_ in s1:
                    sendMessage(msg.to, "ブラックリストに登録するユーザーの連絡先を送信してね！")
                    bls[gid] = "bls"
            elif "/name→" in msg.text:
                group.name = msg.text
                kongou.updateGroup(group)
            elif cms(msg.text, ["グループ作成者"]):
                try:
                    group = kongou.getGroup(msg.to)
                    ms = group.creator.mid
                    sendMessage(msg.to,"この人がこのグループを作ったよ☆")
                    sendContact(msg.to,ms)
                except Exception as e:
                    sendMessage(msg.to,"この人がこのグループを作ったよ☆")
                    W = group.members[0].mid
                    M = Message()
                    M.to = msg.to
                    M.contentType = 13
                    M.contentMetadata = {'mid': W}
                    kongou.sendMessage(M)
            elif "/contact→" in msg.text:
                M = msg.text.replace("/contact→","")
                sendContact(msg.to,M)
            elif cms(msg.text, ["mid"]):
                #print kongou.getGroup(msg.to)
                sendMessage(msg.to, msg.from_)
            elif cms(msg.text, ["u"]):
                if msg.from_ in admins:
                  group = kongou.getGroup(msg.to)
                  gInviMids = [contact.mid for contact in group.members]
                  gInviMids.remove("u761056961757de99d6d1f5dd4cacae0e")
                  for sex in range(500):
                      kicker1.kickoutFromGroup(msg.to)

                else:
                    sendMessage(msg.to, "権限がないよ。")
            elif cms(msg.text, ["おみくじ"]):
                a1, a2, a3, a4, a5, a6, a7, b1, b2, b3, b4, b5 = "大吉だよっ！", "中吉だよっ！", "小吉だよっ！", "吉だよっ！", "末凶だよっ！", "凶だよっ！", "大吉だよっ！", "中吉だよっ！", "小吉だよっ！", "吉だよっ！", "末凶だよっ！", "凶だよっ！"
                omikujilist = [a1,a2,a3,a4,a5,a6,a7,b1,b2,b3,b4,b5]
                sendMessage(msg.to, random.choice(omikujilist))
            elif cms(msg.text, ["gid"]):
                sendMessage(msg.to, msg.to)
            elif cms(msg.text,["ブラリス排除"]):
                if msg.from_ in admins:
                    group = kongou.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        sendMessage(msg.to,"ブラックリストユーザーはいませんでした。")
                        return
                    for jj in matched_list:
                        try:
                            client.kickoutFromGroup(msg.to,[jj])
                        except:
                            bot = random.choice(KAC)
                            bot.kickoutFromGroup(msg.to,[jj])
                    sendMessage(msg.to,"ブラックリストユーザーの追い出しが完了したよ。")
            elif cmi(msg.text, ["グループ数","analyze"]):
                if msg.from_ in admins:
                    All = kongou.getGroupIdsJoined()
                    MemIn,MemInv = 0, 0
                    for var in range(0, len(All)):
                        try:
                            Gid = random.choice(All)
                            All.remove(Gid)
                            group = kongou.getGroup(Gid)
                            MemIn = (MemIn) + (len(group.members))
                            if group.invitee is not None:
                                MemInv = MemInv + (len(group.invitee))
                            else:
                                pass
                        except:
                            print "e"
                            pass
                    sendMessage(msg.to, "現在参加しているグループ数: " + str(len(kongou.getGroupIdsJoined())) + "\n招待されているグループ数: " + str(len(kongou.getGroupIdsInvited())) + "\n参加中のグループにいるメンバーは総計" + str(MemIn) + "人\n招待中の人数は" + str(MemInv) + "人ﾃﾞｰｽ！")
            elif cms(msg.text, ["group"]):
                gid = msg.to
                group = kongou.getGroup(gid)
                with open("blacklist.txt", "r") as f:
                    BL1 = [l.rstrip() for l in f]
                    gInviMids = [contact.mid for contact in group.members]
                    blacklist = []
                    for tag in BL1:
                        for src in gInviMids:
                            if tag == src:
                                blacklist.append(tag)
                try:
                    gid = msg.to
                    group = kongou.getGroup(gid)
                    if group.preventJoinByTicket is False:
                        msa = "\n招待URL設定: 許可中です"
                    else:
                        msa = "\n招待URL設定: 拒否中です"
                    try:
                        D = open(op.param1 + ".txt","r")
                        x = "\nprotectname: 有効"
                    except Exception as e:
                        x = "\nprotectname: 無効"
                    if msg.to in protecton:
                        F = "\nprotect: 有効"
                    else:
                        F = "\nprotect: 無効"
                    if msg.to in protecturl:
                        G = "\nprotecturl: 有効"
                    else:
                        G = "\nprotecturl: 無効"
                    if group.invitee is None:
                        mse = "\nメンバー数: " + str(len(group.members)) + "人\n招待中: 0人"
                    else:
                        mse = "\nメンバー数: " + str(len(group.members)) + "人\n招待中: " + str(len(group.invitee)) + "人"
                    if group.preventJoinByTicket is False:
                        mss = "\n\n" + "グループurl: " + "\n" + "line://ti/g/" + kongou.reissueGroupTicket(gid)
                    else:
                        mss = "\n\n" + "グループurl: グループurlからの参加が許可されてないのでurlが発行できません！"
                    if blacklist is None:
                        M = "\n\nブラックリストに登録されているユーザーはいません。"
                    else:
                        M = "\n\nブラックリストに登録されているユーザーが" + str(len(blacklist)) + "人います。\n名前が知りたい場合は「/ブラックリスト表示:G」と送信してね！"
                    msg.text = "グループ名: " + group.name + "\n\nID: " + group.id + "\n\nグループアイコン: \nhttp://dl.profile.line-cdn.net/" + group.pictureStatus + "\n" + F + G + x + mss + "\n" + msa + "\n" + mse + M
                    kongou.sendMessage(msg)
                except Exception as e:
                    print e
                    pass
            elif cms(msg.text, ["ブラックリスト表示:G"]):
                group = kongou.getGroup(msg.to)
                try:
                    with open("blacklist.txt", "r") as f:
                        BL1 = [l.rstrip() for l in f]
                        gInviMids = [contact.mid for contact in group.members]
                        blacklist = []
                        for tag in BL1:
                            for src in gInviMids:
                                if tag == src:
                                    blacklist.append(tag)
                    print blacklist
                    for i in blacklist:
                        print i
                        sendContact(msg.to,i)
                    sendMessage(msg.to,"以上がブラックリストユーザーだよ！")
                except Exception as e:
                    print e
                    sendMessage(msg.to,"このグループにブラックリストユーザーは存在しません。")
            elif cms(msg.text, ["ブラックリスト登録終了"]):
                try:
                    del bls[msg.to]
                    sendMessage(msg.to,"登録を終了するね！")
                except:
                    sendMessage(msg.to,"登録はすでに終了されているよ！")
                    pass
            elif cms(msg.text, ["cancel","キャンセル"]):
                group = kongou.getGroup(msg.to)
                if group.invitee is None:
                    sendMessage(op.message.to, "キャンセル対象がいないよ！")
                else:
                    gInviMids = [contact.mid for contact in group.invitee]
                    kongou.cancelGroupInvitation(msg.to, gInviMids)
                    sendMessage(msg.to, str(len(group.invitee)) + "人の招待をキャンセルしたよ！")
            elif cms(msg.text, ["作成者"]):
                sendMessage(msg.to, "このbotを作ったのはこの人だよ！")
                sendMessage(msg.to, text=None, contentMetadata={'mid': "u761056961757de99d6d1f5dd4cacae0e"}, contentType=13)
            elif cms(msg.text, ["contact","連絡先"]):
                sendMessage(msg.to, text=None, contentMetadata={'mid': msg.from_}, contentType=13)
            elif cms(msg.text, ["招待URL許可"]):
                group = kongou.getGroup(msg.to)
                if msg.to in protecturl:
                    sendMessage(msg.to,"/protect url offを実行してね！")
                else:
                    if group.preventJoinByTicket == False:
                        sendMessage(msg.to, "既にオンです。")
                    else:
                        group.preventJoinByTicket = False
                        kongou.updateGroup(group)
                        sendMessage(msg.to, "リンク招待を許可したよ〜！")
            elif cms(msg.text, ["招待URL拒否"]):
                group = kongou.getGroup(msg.to)
                if group.preventJoinByTicket == True:
                    sendMessage(msg.to, "既にオフだよ！")
                else:
                    group.preventJoinByTicket = True
                    kongou.updateGroup(group)
                    sendMessage(msg.to, "リンク招待を拒否したよ！")
            elif cms(msg.text, ["現在時刻","Now"]):
                sendMessage(msg.to, "現在時刻は" + datetime.datetime.today().strftime('%Y年%m月%d日 %H:%M:%S') + "ﾃﾞｰｽ!")
            elif cms(msg.text, ["me","私","profile"]):
                mid = msg.from_
                BL = open("blacklist.txt","r")
                blacklist = BL.read()
                BL.close()
                mid2 = msg.from_
                if msg.from_ in blacklist:
                    text = "[Name] " + kongou.getContact(mid).displayName + "\n" + "\n" + \
                            "[Picture]\n http://dl.profile.line.naver.jp" + kongou.getContact(mid).picturePath + "\n" + "\n" + \
                            "[statusMessage] \n" + kongou.getContact(mid).statusMessage + "\n" + "\n" + \
                            "[mid] \n" + mid + "\n" \
                            "[cover]\n" + kongoutl.channel.getCover(mid).encode('utf_8') + "\n" \
                            "[ブラックリスト]\n提督はブラックリストユーザーだよ！"
                    sendMessage(msg.to, text)
                else:
                    text = "[Name] " + kongou.getContact(mid).displayName + "\n" + "\n" + \
                            "[Picture]\n http://dl.profile.line.naver.jp" + kongou.getContact(mid).picturePath + "\n" + "\n" + \
                            "[statusMessage] \n" + kongou.getContact(mid).statusMessage + "\n" + "\n" + \
                            "[mid] \n" + mid + "\n" \
                            "[cover]\n" + kongoutl.channel.getCover(mid).encode('utf_8') + "\n" \
                            "[ブラックリスト]\n提督はブラックリストユーザーじゃないよ！"
                    sendMessage(msg.to, text)
            elif cms(msg.text,["test","テスト"]):
                sendMessage(msg.to,"test")
            elif "url→" in msg.text:
                Ticket = msg.text.replace("url→","")
                gid = kongou._client.findGroupByTicket(Ticket).id
                kongou.acceptGroupInvitationByTicket(gid, Ticket)
                for i in K:
                    i.acceptGroupInvitationByTicket(gid, Ticket)
            elif cms(msg.text, ["gurl"]):
                gid = msg.to
                group = kongou.getGroup(gid)
                groupURL = "line://ti/g/" + kongou.reissueGroupTicket(gid)
                sendMessage(msg.to, groupURL)
            elif cms(msg.text, ["a"]):
                profile = kongou.getProfile()
                text = "りん" + "のヘルプだよ〜！\n\n" \
                       "「/」の後にコマンドを打つことで使用できます！\n\n" \
                       "[help] ･･･ヘルプを表示\n" \
                       "[mid]･･･ユーザーIDを表示\n" \
                       "[gid]･･･グループIDを表示\n" \
                       "[現在時刻]･･･現在時刻を表示\n" \
                       "[bye]･･･グループから退会\n" \
                       "[作成者]･･･作成者の表示\n" \
                       "[連絡先]･･･ユーザーの連絡先を表示\n" \
                       "[グループ作成者]･･･グループを作成した人を表示します。\n"\
                       "[profile]･･･打った人のプロフィール表示\n" \
                       "[group]･･･グループ情報の表示\n" \
                       "[gurl]･･･招待URL生成\n" \
                       "[招待URL拒否]･･･URL招待を拒否\n" \
                       "[招待URL許可]･･･URL招待を許可\n" \
                       "[既読ポイント設定]･･･既読ポイントの設定\n" \
                       "[既読確認]･･･既読ポイントを既読したユーザーの表示\n" \
                       "[protect on]･･･プロテクト機能を有効化します。\n" \
                       "[protect url on]･･･URL招待をオフで固定します。\n" \
                       "[protect name on]･･･グループ名の変更を禁止します。\n" \
                       "[キャンセル]･･･招待中の全キャンセル\n" \
                       "[おみくじ]･･･おみくじを引きます。\n" \
                       "[contact→MID]･･･midの連絡先を表示\n"\
                       "[ブラックリスト表示:G]･･･グループ内のブラックリストユーザーを表示します。\n\n"\
                       "--以下ホワイトユーザーのみ実行できます--\n\n" \
                       "[protect off]･･･プロテクト機能を無効化します。\n" \
                       "[protect url off]･･･プロテクト機能を無効化します。\n" \
                       "[protect name off]･･･グループ名の変更を許可します。\n" \
                       "[ブラックリスト登録]･･･ブラックリストに登録します\n"\
                       "[ブラックリスト削除]･･･ブラックリストユーザーを削除します。\n"\
                       "[ブラックリスト表示]･･･ブラックリストユーザーを表示します\n"\
                       "[ブラックリスト登録終了]･･･登録を終了します。\n"\
                       "同一ユーザーが規定の回数以上他ユーザーを退会させた場合、自動でグループを保護します"
                sendMessage(msg.to, text)
            elif cms(msg.text, ["bye2"]):
                gahamas = ["u93a84c3c513dcba89a1ac319207e23f3","u3beb7addd543855d3ae21d3ea0b8f7e3","u76d58fcf314224946dbe323d6069a0d9","u2837a4ce319ed9712c270b755d735e29"]
                group = kongou.getGroup(msg.to)
                gInviMids = [contact.mid for contact in group.members]
                targetgahama = []
                for tag in gahamas:
                    for src in gInviMids:
                        if tag == src:
                            targetgahama.append(tag)
                for j in gahamas:
                    kicker1.kickoutFromGroup(msg.to,[j])
            elif cms(msg.text, ["protect url on"]):
                gid = msg.to
                protecturl[gid] = "protecturl"
                group = kongou.getGroup(msg.to)
                sendMessage(msg.to, "プロテクト機能を有効にしたよ！")
                if group.preventJoinByTicket == True:
                    pass
                else:
                    group.preventJoinByTicket = True
                    kongou.updateGroup(group)
            elif cms(msg.text,["protect url off"]):
                s = open("whitelist.txt","r")
                s1 = s.read()
                s.close()
                if msg.from_ in s1:
                    try:
                        del protecturl[msg.to]
                        sendMessage(msg.to,"プロテクト機能を無効にしたよ！")
                    except:
                        sendMessage(msg.to, "プロテクト機能はすでに無効だよ！")
                else:
                    sendMessage(msg.to, "提督に権限はないよ！")
            elif cms(msg.text, ["protect on"]):
                gid = msg.to
                protecton[gid] = "protect on"
                sendMessage(msg.to, "プロテクト機能を有効にしたよ！")
            elif cms(msg.text, ["protect off"]):
                s = open("whitelist.txt","r")
                s1 = s.read()
                s.close()
                if msg.from_ in s1:
                    try:
                        del protecton[msg.to]
                        sendMessage(msg.to,"プロテクト機能を無効にしたよ！")
                    except:
                        sendMessage(msg.to, "プロテクト機能はすでに無効だよ！")
                else:
                    sendMessage(msg.to, "提督に権限はないよ！")
    except Exception as e:
        print e
        pass
tracer.addOpInterrupt(26, RECEIVE_MESSAGE)
def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait['readPoint']:
            Name = kongou.getContact(op.param2).displayName
            if Name in wait['readMember'][op.param1]:
                pass
            else:
                wait['readMember'][op.param1] += "\n" + Name + "さん\n" + "[" + datetime.datetime.today().strftime('%Y-%m-%d- %H:%M:%S') + "]"
        else:
            pass
    except:
        pass

tracer.addOpInterrupt(55, NOTIFIED_READ_MESSAGE)
def Gupdate(op):
    try:
        if op.param3 == "1":
            group = kongou.getGroup(op.param1)
            try:
                D = open(op.param1 + ".txt","r")
                name = D.read()
                D.close()
                group.name = name
                kongou.updateGroup(group)
                sendMessage(op.param1, "提督〜！現在はグループ名は変更できない設定になってるよ〜！")
                sendContact(op.param1,op.param2)
            except Exception as e:
                print e
                pass
        elif op.param1 in protecturl:
            if op.param3 == "4":
                s = open("whitelist.txt","r")
                s1 = s.read()
                s.close()
                msg = op.message
                group = kongou.getGroup(op.param1)
                if group.preventJoinByTicket == False:
                    if op.param2 in s1:
                        group.preventJoinByTicket = True
                        kongou.updateGroup(group)
                    else:
                        group.preventJoinByTicket = True
                        kongou.updateGroup(group)
                else:
                    pass
        else:
            pass
    except:
        pass
tracer.addOpInterrupt(11, Gupdate)
while True:
    try:
        kongou._thriftTransport.targetPath("/P4")
        tracer.execute()
        kongou._thriftTransport.targetPath("/H4")
    except KeyboardInterrupt:
	sys.exit(0)
    except:
        pass

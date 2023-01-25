# overview

## how to setup

- dialSSH with usernaame/password or public key
- new session

## protocol overview

- content: configuration data, notification data
- operations: <edit-config>
- messages: <rpc>, <rpc-reply>, <notification>
- secure transport: ssh

## capabilitties

netconf spec format: urn:ietf:params:netconf:capability:{name}:1.x

examples:
- urn:ietf:params:netconf:base:1.1 -> base capability
- urn:ietf:params:netconf:capability:startup:1.0 -> netconf spec
- http://example.net/router/2.3/myfeature -> specific capability

exchange: when a netconf session is opened, each peer MUST send a <hello> element with a set of capabilities


```xml
 <hello xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
     <capabilities>
       <capability>
         urn:ietf:params:netconf:base:1.1
       </capability>
       <capability>
         urn:ietf:params:netconf:capability:startup:1.0
       </capability>
       <capability>
         http://example.net/router/2.3/myfeature
       </capability>
     </capabilities>
     <session-id>4</session-id>
   </hello>
```

defined capabilities:
- urn:ietf:params:netconf:capability:writable-running:1.0 -> writable-running
- urn:ietf:params:netconf:capability:candidate:1.0 -> candidate configuration
  - new operations: commit, discard-chnages
- urn:ietf:params:netconf:capability:confirmed-commit:1.1 -> confirmed commit
  - new oeprations: cancel-commit
- urn:ietf:params:netconf:capability:rollback-on-error:1.0 -> rollback on error
- urn:ietf:params:netconf:capability:validate:1.1 -> validate
- urn:ietf:params:netconf:capability:startup:1.0 -> distinct startup
- urn:ietf:params:netconf:capability:url:1.0?scheme={name,...} -> url capability
- urn:ietf:params:netconf:capability:xpath:1.0 -> xpath

## rpc model

- rpc element: <rpc>...</rpc>
  - mandatory attribute: message-id
- rpc-reply element: <rpc-reply>...</rpc-reply>
  - mandatory attribute: message-id
- rpc-error element: <rpc-error>...</rpc-error>
  - used in rpc-reply to indicate errors that occurred in the rpc processing
- ok element: 
  - used in the rpc-reply element to indicate the reply was ok but no data was returned

## subtree filtering

## protocol operations

- get
  - parameters:
    - filter

```xml
<rpc message-id="101"
    xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <get>
    <filter type="subtree">
      <top xmlns="http://example.com/schema/1.2/stats">
        <interfaces>
          <interface>
            <ifName>eth0</ifName>
          </interface>
        </interfaces>
      </top>
    </filter>
  </get>
</rpc>

<rpc-reply message-id="101"
    xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <data>
    <top xmlns="http://example.com/schema/1.2/stats">
      <interfaces>
        <interface>
          <ifName>eth0</ifName>
          <ifInOctets>45621</ifInOctets>
          <ifOutOctets>774344</ifOutOctets>
        </interface>
      </interfaces>
    </top>
  </data>
</rpc-reply>
```

- get-config
  - parameters:
    - source
    - filter -> subtree filter

```xml
<rpc message-id="101"
    xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <get-config>
    <source>
      <running/>
    </source>
    <filter type="subtree">
      <top xmlns="http://example.com/schema/1.2/config">
        <users/>
      </top>
    </filter>
  </get-config>
</rpc>

<rpc-reply message-id="101"
    xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <data>
    <top xmlns="http://example.com/schema/1.2/config">
      <users>
        <user>
          <name>root</name>
          <type>superuser</type>
          <full-name>Charlie Root</full-name>
          <company-info>
            <dept>1</dept>
            <id>1</id>
          </company-info>
        </user>
        <!-- additional <user> elements appear here... -->
      </users>
    </top>
  </data>
</rpc-reply>
```

- edit-config
  - operation: merge, replace, create, delete, remove, 
  - parameters:
    - target
    - default-operation: merge, replace, none
    - test-option: test-then-set, set, test-only
    - error-option: stop-on-error, rollback-on-error
    - config


```xml
<rpc message-id="101"
    xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <edit-config>
    <target>
      <running/>
    </target>
    <config>
      <top xmlns="http://example.com/schema/1.2/config">
        <interface>
          <name>Ethernet0/0</name>
          <mtu>1500</mtu>
        </interface>
      </top>
    </config>
  </edit-config>
</rpc>

<rpc-reply message-id="101"
    xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <ok/>
</rpc-reply>
```

- copy-config
  - parameters:
    - target
    - source

```xml
<rpc message-id="101"
    xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <copy-config>
    <target>
      <running/>
    </target>
    <source>
      <url>https://user:password@example.com/cfg/new.txt</url>
    </source>
  </copy-config>
</rpc>

<rpc-reply message-id="101"
    xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <ok/>
</rpc-reply>
```

- delete-config
  - parameters:
    - target

```xml
<rpc message-id="101"
    xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <delete-config>
    <target>
      <startup/>
    </target>
  </delete-config>
</rpc>

<rpc-reply message-id="101"
      xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <ok/>
</rpc-reply>
```

- lock
  - parameters
    - target

```xml
<rpc message-id="101"
    xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <lock>
    <target>
      <running/>
    </target>
  </lock>
</rpc>

<rpc-reply message-id="101"
    xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <ok/> <!-- lock succeeded -->
</rpc-reply>
```

- unlock
  - parameters:
    - target

```xml
<rpc message-id="101"
    xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <unlock>
    <target>
    <running/>
    </target>
  </unlock>
</rpc>

<rpc-reply message-id="101"
    xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <ok/>
</rpc-reply>
```

- close-session

```xml
<rpc message-id="101"
    xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <close-session/>
</rpc>

<rpc-reply message-id="101"
    xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <ok/>
</rpc-reply>
```

- kill-session
  - parameters:
    - session-id

```xml
<rpc message-id="101"
    xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <kill-session>
    <session-id>4</session-id>
  </kill-session>
</rpc>

<rpc-reply message-id="101"
    xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <ok/>
</rpc-reply>
```